from __future__ import annotations
from queue import SimpleQueue

import grpc
from proto.remote.kv_pb2 import Cursor, Op
from proto.remote.kv_pb2_grpc import KVStub


class ErigonKV:
    def __init__(self, private_api="127.0.0.1:9090"):
        self.channel = grpc.insecure_channel(private_api)
        self.stub = KVStub(self.channel)
        self.queue = SimpleQueue()
        self.reply = self.stub.Tx(iter(self.queue.get, None))
        self.transaction = next(self.reply)

    def open(self, bucket, dup_sort=False):
        op = Cursor(op=Op.OPEN_DUP_SORT if dup_sort else Op.OPEN, bucketName=bucket)
        self.queue.put(op)
        self.cursor = next(self.reply).cursorID

    def read(self, op, k=None):
        op = Cursor(op=op, cursor=self.cursor, k=k)
        self.queue.put(op)
        return next(self.reply)


class AsyncErigonKV:
    async def connect(self, private_api="127.0.0.1:9090"):
        self.channel = grpc.aio.insecure_channel(private_api)
        self.stub = KVStub(self.channel)
        self.conn = self.stub.Tx()
        await self.conn.read()

    def open(self, bucket) -> AsyncErigonCursor:
        return AsyncErigonCursor(self.conn, bucket)


class AsyncErigonCursor:
    def __init__(self, conn, bucket):
        self.conn = conn
        self.bucket = bucket

    async def __aenter__(self):
        await self.conn.write(Cursor(op=Op.OPEN, bucketName=self.bucket))
        cursor = await self.conn.read()
        self.cursor = cursor.cursorID
        return self

    def __aiter__(self):
        return self

    async def __anext__(self):
        await self.conn.write(Cursor(op=Op.NEXT, cursor=self.cursor))
        return await self.conn.read()

    async def __aexit__(self, exc_t, exc_v, exc_tb):
        pass


async def connect(private_api="127.0.0.1:9090"):
    kv = AsyncErigonKV()
    await kv.connect(private_api)
    return kv
