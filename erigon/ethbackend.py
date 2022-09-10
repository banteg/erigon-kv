import asyncio

import grpc
from devtools import debug

from erigon.proto.remote.ethbackend_pb2 import BlockRequest
from erigon.proto.remote.ethbackend_pb2_grpc import ETHBACKENDStub
from erigon.types import decode_block, encode_hash


class ErigonEthBackend:
    async def connect(self, private_api="127.0.0.1:9090"):
        self.channel = grpc.aio.insecure_channel(private_api)
        self.stub = ETHBACKENDStub(self.channel)

    async def get_block(self, block_number: int, block_hash: bytes):
        reply = await self.stub.Block(
            BlockRequest(blockHeight=block_number, blockHash=encode_hash(block_hash))
        )
        return decode_block(reply.blockRlp)


async def main():
    rpc = ErigonEthBackend()
    await rpc.connect()
    block = await rpc.get_block(
        15510461, bytes.fromhex("10323a62497dd5ecaec4654e5b79d99959513a24891178bfbb49c0b874bee258")
    )
    debug(block.as_dict())


if __name__ == "__main__":
    asyncio.run(main())
