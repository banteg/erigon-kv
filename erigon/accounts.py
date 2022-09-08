import asyncio
import enum
import io
from typing import Optional

from devtools import debug
from eth_utils import encode_hex, to_canonical_address
from hexbytes import HexBytes
from pydantic import BaseModel
from typer import Typer

from erigon.kv import ErigonKV, Op

app = Typer()


class AccountFieldSet(enum.IntFlag):
    nonce = 1
    balance = 2
    incarnation = 4
    code_hash = 8


def read_int(stream):
    length = int.from_bytes(stream.read(1), "big")
    return int.from_bytes(stream.read(length), "big")


class Account(BaseModel):
    nonce: int = 0
    balance: int = 0
    incarnation: int = 0  # 0 - not set, contracts start with 1, increased by selfdestruct + create2
    code_hash: Optional[bytes] = None

    @classmethod
    def from_storage(cls, data: bytes):
        account = cls()
        stream = io.BytesIO(data)
        field_set = AccountFieldSet(int.from_bytes(stream.read(1), "big"))

        if AccountFieldSet.nonce in field_set:
            account.nonce = read_int(stream)

        if AccountFieldSet.balance in field_set:
            account.balance = read_int(stream)

        if AccountFieldSet.incarnation in field_set:
            account.incarnation = read_int(stream)

        if AccountFieldSet.code_hash in field_set:
            length = int.from_bytes(stream.read(1), "big")
            assert length == 32, "invalid encoding"
            account.code_hash = stream.read(length)

        return account


async def read_account(kv: ErigonKV, canonical_address: bytes):
    async with kv.open("PlainState") as cursor:
        row = await cursor.seek_exact(canonical_address)
        account = Account.from_storage(row.v)
        return account


async def read_code(kv: ErigonKV, code_hash: bytes):
    async with kv.open("Code") as cursor:
        row = await cursor.seek_exact(code_hash)
        return row.v


async def read_storage(kv: ErigonKV, canonical_address: bytes, account: Account):
    if account.incarnation == 0:
        return {}

    async with kv.open("PlainState", dup_sort=True) as cursor:
        prefix = canonical_address + account.incarnation.to_bytes(8, "big")
        storage = {}
        # [account:20][incarnation:8][key:32] | [value:32]
        row = await cursor.seek_exact(prefix)
        storage[row.v[:32]] = row.v[32:]

        async for row in cursor:
            debug(row.k.hex(), row.v.hex())
            if not row.k.startswith(prefix):
                break
            # no key | [key:32][value:32]
            storage[row.k[-32:]] = row.v.rjust(32, b"\x00")

        return storage


async def test_all(address: str):
    canonical_address = to_canonical_address(address)

    kv = ErigonKV()
    await kv.connect()

    account = await read_account(kv, canonical_address)
    debug(account)

    code = await read_code(kv, account.code_hash)
    debug(code)

    storage = await read_storage(kv, canonical_address, account)
    debug(storage)


@app.command()
def main(address: str):
    account = asyncio.run(test_all(address))
    debug(account)


if __name__ == "__main__":
    app()
