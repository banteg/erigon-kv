import asyncio

import rlp
from devtools import debug
from eth.vm.forks.london.headers import LondonBackwardsHeader

from erigon.kv import ErigonKV


def decode_block_header(data: bytes):
    return rlp.decode(data, sedes=LondonBackwardsHeader)


async def test_all():
    kv = ErigonKV()
    await kv.connect()

    async with kv.open("Header") as cursor:
        async for row in cursor:
            debug(decode_block_header(row.v))


if __name__ == "__main__":
    asyncio.run(test_all())
