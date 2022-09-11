import asyncio
import enum
import io
from typing import Optional

from devtools import debug
from eth_utils import encode_hex, to_canonical_address
from pydantic import BaseModel
from typer import Typer

from erigon.kv import ErigonKV, Op
from erigon.types import decode_account, Account

app = Typer()


async def read_account(kv: ErigonKV, canonical_address: bytes):
    async with kv.open("PlainState") as cursor:
        row = await cursor.seek_exact(canonical_address)
        account = decode_account(row.v)
        return account


async def read_code(kv: ErigonKV, code_hash: bytes):
    async with kv.open("Code") as cursor:
        row = await cursor.seek_exact(code_hash)
        return row.v


async def read_storage(kv: ErigonKV, canonical_address: bytes, incarnation: int):
    assert incarnation > 0, "eoa has no storage"

    async with kv.open("PlainState") as cursor:
        prefix = canonical_address + incarnation.to_bytes(8, "big")
        storage = {}
        # [account:20][incarnation:8][key:32] | [value:32]
        row = await cursor.seek_exact(prefix)
        storage[row.v[:32]] = row.v[32:]

        async for row in cursor:
            if not row.k.startswith(prefix):
                break
            # no key | [key:32][value:32]
            storage[row.k[-32:]] = row.v

        return storage


async def test_all(address: str):
    canonical_address = to_canonical_address(address)

    kv = ErigonKV()
    await kv.connect()

    account = await read_account(kv, canonical_address)
    debug(account)

    code = await read_code(kv, account.code_hash)
    debug(code)

    storage = await read_storage(kv, canonical_address, account.incarnation)
    debug({encode_hex(k): encode_hex(v) for k, v in storage.items()})


@app.command()
def main(address: str):
    account = asyncio.run(test_all(address))
    debug(account)


if __name__ == "__main__":
    app()
