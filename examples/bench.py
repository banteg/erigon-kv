import asyncio

from devtools import debug
from humanize import naturalsize

from erigon.ethbackend import ErigonEthBackend
from erigon.kv import ErigonKV
from erigon.proto.remote.ethbackend_pb2 import BlockRequest
from erigon.types import decode_block, encode_hash, to_bytes, to_int


async def main():
    kv = ErigonKV()
    await kv.connect()

    eth = ErigonEthBackend()
    await eth.connect()

    n = 0
    txs = 0
    read = 0
    t = debug.timer(dp=6).start()
    t_block = debug.timer(dp=6)
    t_rlp = debug.timer(dp=6)

    async with (
        kv.open("CanonicalHeader") as canonical,
        kv.open("Header") as headers,
    ):
        # most headers are in snapshots, ~120k last ones are in the db
        await headers.seek(to_bytes(1))

        async for row in headers:
            block_number = to_int(row.k[:8])
            canon = await canonical.seek_exact(row.k[:8])
            if canon.v != row.k[8:]:
                continue

            # read block
            n += 1
            with t_block(verbose=False):
                resp = await eth.stub.Block(
                    BlockRequest(
                        blockHeight=block_number,
                        blockHash=encode_hash(canon.v),
                    )
                )
                read += len(resp.blockRlp)

            with t_rlp(verbose=False):
                block = decode_block(resp.blockRlp)
                txs += len(block.transactions)

            if block_number % 1000 == 0:
                t.capture(verbose=False)
                elapsed = t.results[-1].elapsed()
                print(
                    {
                        "block": block_number,
                        "elapsed": elapsed,
                        "n": n,
                        "txs": txs,
                        "read": naturalsize(read),
                        "block/s": n / elapsed,
                        "txs/s": txs / elapsed,
                        "read/s": naturalsize(read / elapsed),
                    }
                )

        t.summary(verbose=False)
        print("get block", end=" ")
        t_block.summary(verbose=False)
        print("decode block", end=" ")
        t_rlp.summary(verbose=False)


if __name__ == "__main__":
    asyncio.run(main())
