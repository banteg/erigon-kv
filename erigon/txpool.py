import asyncio

import grpc
from devtools import debug
from google.protobuf.empty_pb2 import Empty
from pydantic import BaseModel

from erigon.proto.txpool.txpool_pb2 import OnAddRequest
from erigon.proto.txpool.txpool_pb2_grpc import TxpoolStub
from erigon.types import Transaction, decode_hash, decode_transaction


class Tx(BaseModel):
    sender: bytes
    transaction: Transaction
    is_local: bool

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def from_message(cls, msg):
        return cls(
            sender=decode_hash(msg.sender),
            transaction=decode_transaction(msg.rlpTx),
            is_local=msg.isLocal,
        )


class ErigonTxPool:
    async def connect(self, private_api="127.0.0.1:9090"):
        options = [("grpc.max_receive_message_length", 2**30)]
        self.channel = grpc.aio.insecure_channel(private_api, options=options)
        self.stub = TxpoolStub(self.channel)

    async def pending(self):
        reply = await self.stub.Pending(Empty())
        for tx in reply.txs:
            debug(Tx.from_message(tx))

    async def watch(self):
        added = self.stub.OnAdd(OnAddRequest())
        async for reply in added:
            for tx in reply.rplTxs:
                debug(decode_transaction(tx))


async def main():
    changes = ErigonTxPool()
    await changes.connect()
    await changes.pending()
    await changes.watch()


if __name__ == "__main__":
    asyncio.run(main())
