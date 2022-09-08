import grpc
from proto.remote.kv_pb2 import Cursor, Op
from proto.remote.kv_pb2_grpc import KVStub
import asyncio
from devtools import debug
import itertools
import time
from humanize import naturalsize

async def main():
    start = time.perf_counter()
    channel = grpc.aio.insecure_channel('127.0.0.1:9090')
    stub = KVStub(channel)
    call = stub.Tx()
    
    txid = await call.read()
    debug(txid)
    
    await call.write(Cursor(op=Op.OPEN, bucketName='Code'))
    curid = await call.read()
    debug(curid)

    bytes_read = 0
    for i in itertools.count(1):
        await call.write(Cursor(op=Op.NEXT, cursor=curid.cursorID))
        row = await call.read()
        if row.k == b'':
            break
        bytes_read += len(row.v)
        if i % 10000 == 0:
            elapsed = time.perf_counter() - start
            print(i, row.k[:8].hex(), f'{elapsed:.3f}s {i / elapsed:,.0f}/s {naturalsize(bytes_read)} {naturalsize(bytes_read / elapsed)}/s')


if __name__ == '__main__':
    asyncio.run(main())
