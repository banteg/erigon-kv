import enum
import io
from typing import Optional

from devtools import debug
from eth_utils import to_canonical_address
from pydantic import BaseModel
from typer import Typer

from hexbytes import HexBytes
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
    incarnation: Optional[int] = None
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

    def read_code(self):
        assert self.code_hash, "no code"
        kv = ErigonKV()
        kv.open("Code")
        data = kv.read(Op.SEEK_EXACT, k=self.code_hash)
        return data.v


@app.command()
def read_account(address: str):
    canonical_address = to_canonical_address(address)
    kv = ErigonKV()
    kv.open("PlainState")
    data = kv.read(Op.SEEK_EXACT, k=canonical_address)
    assert data.k == canonical_address, "account not found"
    account = Account.from_storage(data.v)
    debug(account)
    return account


if __name__ == "__main__":
    app()
