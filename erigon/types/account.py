import enum
import io
from typing import Optional

from pydantic import BaseModel

from erigon.types import to_int


class AccountFieldSet(enum.IntFlag):
    nonce = 1
    balance = 2
    incarnation = 4
    code_hash = 8


class Account(BaseModel):
    nonce: int = 0
    balance: int = 0
    incarnation: int = 0  # contracts start with 1
    code_hash: Optional[bytes]


def read_int(stream, size: int = None):
    """
    read a length-prefixed big-endian integer from a stream
    """
    if size is None:
        size = to_int(stream.read(1))

    return to_int(stream.read(size))


def decode_account(data: bytes):
    account = Account()
    stream = io.BytesIO(data)
    field_set = AccountFieldSet(to_int(stream.read(1)))

    if AccountFieldSet.nonce in field_set:
        account.nonce = read_int(stream)

    if AccountFieldSet.balance in field_set:
        account.balance = read_int(stream)

    if AccountFieldSet.incarnation in field_set:
        account.incarnation = read_int(stream)

    if AccountFieldSet.code_hash in field_set:
        length = to_int(stream.read(1))
        assert length == 32, "invalid encoding"
        account.code_hash = stream.read(length)

    return account
