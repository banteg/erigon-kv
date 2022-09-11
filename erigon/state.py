import asyncio

import grpc
from devtools import debug
from pydantic import BaseModel

from erigon.accounts import Account
from erigon.proto.remote.kv_pb2 import StateChangeRequest
from erigon.proto.remote.kv_pb2_grpc import KVStub
from erigon.types import decode_hash, decode_transaction, Transaction
from devtools import PrettyFormat
from enum import IntEnum

from erigon.types.account import decode_account

pp = PrettyFormat(repr_strings=True)


class Action(IntEnum):
    STORAGE = 0
    UPSERT = 1
    CODE = 2
    UPSERT_CODE = 3
    REMOVE = 4


class AccountChange(BaseModel):
    address: bytes
    incarnation: int
    action: Action
    data: Account
    code: bytes
    storage_changes: dict

    @classmethod
    def from_message(cls, msg):
        return cls(
            address=decode_hash(msg.address),
            incarnation=msg.incarnation,
            action=Action(msg.action),
            data=decode_account(msg.data),
            code=msg.code,
            storage_changes={decode_hash(x.location): x.data for x in msg.storageChanges},
        )


class StateChange(BaseModel):
    direction: int
    block_height: int
    block_hash: bytes
    changes: list[AccountChange]
    txs: list[Transaction]

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_message(cls, msg):
        txs = []
        for tx in msg.txs:
            txs.append(decode_transaction(tx))

        changes = [AccountChange.from_message(x) for x in msg.changes]

        return cls(
            direction=msg.direction,
            block_height=msg.blockHeight,
            block_hash=decode_hash(msg.blockHash),
            changes=changes,
            txs=txs,
        )


class ErigonStateChanges:
    async def connect(self, private_api="127.0.0.1:9090"):
        self.channel = grpc.aio.insecure_channel(private_api)
        self.stub = KVStub(self.channel)

    async def open(self):
        changes = self.stub.StateChanges(StateChangeRequest())
        async for item in changes:
            for change in item.changeBatch:
                pretty = StateChange.from_message(change)
                print(pp(pretty, highlight=True))
                break


async def main():
    changes = ErigonStateChanges()
    await changes.connect()
    await changes.open()


if __name__ == "__main__":
    asyncio.run(main())
