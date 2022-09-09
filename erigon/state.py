import asyncio

import grpc
import rlp
from devtools import debug
from eth.vm.forks.berlin.transactions import AccessListTransaction
from eth.vm.forks.london.transactions import (
    DynamicFeeTransaction,
    LondonLegacyTransaction,
    LondonTypedTransaction,
)
from pydantic import BaseModel

from erigon.proto.remote.kv_pb2 import StateChangeRequest
from erigon.proto.remote.kv_pb2_grpc import KVStub
from erigon.types import decode, encode


class StorageChange(BaseModel):
    location: bytes
    data: bytes


class AccountChange(BaseModel):
    address: bytes
    incarnation: int
    action: int
    data: bytes
    code: bytes
    storage_changes: list[StorageChange]


class StateChange(BaseModel):
    direction: int
    block_height: int
    block_hash: bytes
    changes: list[AccountChange]
    txs: list[LondonLegacyTransaction | AccessListTransaction | DynamicFeeTransaction]

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_message(cls, msg):
        txs = []
        for tx in msg.txs:
            # an rlp list indicates a legacy transaction
            if tx[0] >= 0xC0:
                txs.append(rlp.decode(tx, sedes=LondonLegacyTransaction))
            else:
                txs.append(rlp.decode(tx, sedes=LondonTypedTransaction)._inner)

        return cls(
            direction=msg.direction,
            block_height=msg.blockHeight,
            block_hash=decode(msg.blockHash),
            changes=[],
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
                debug(pretty)
                break


async def main():
    changes = ErigonStateChanges()
    await changes.connect()
    await changes.open()


if __name__ == "__main__":
    asyncio.run(main())
