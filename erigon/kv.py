from contextlib import asynccontextmanager

import grpc
from proto.remote.kv_pb2 import Cursor, Op
from proto.remote.kv_pb2_grpc import KVStub


class ErigonKV:
    async def connect(self, private_api="127.0.0.1:9090"):
        self.channel = grpc.aio.insecure_channel(private_api)
        self.stub = KVStub(self.channel)
        self.conn = self.stub.Tx()
        await self.conn.read()

    @asynccontextmanager
    async def open(self, bucket):
        """
        async with kv.open('bucket') as cursor:
            await cursor.seek(b'prefix')

            async for row in cursor:
                print(row)
        """
        await self.conn.write(Cursor(op=Op.OPEN, bucketName=bucket))
        cursor = await self.conn.read()
        try:
            yield ErigonCursor(self.conn, cursor.cursorID)
        finally:
            await self.conn.write(Cursor(op=Op.CLOSE, cursor=cursor.cursorID))
            await self.conn.read()


class ErigonCursor:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def __aiter__(self):
        return self

    async def __anext__(self):
        await self.conn.write(Cursor(op=Op.NEXT, cursor=self.cursor))
        row = await self.conn.read()
        if row.k == b'':
            raise StopAsyncIteration
        return row

    async def seek(self, key):
        await self.conn.write(Cursor(op=Op.SEEK, k=key, cursor=self.cursor))
        return await self.conn.read()
