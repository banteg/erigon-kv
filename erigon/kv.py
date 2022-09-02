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

    def open(self, bucket):
        op = Cursor(op=Op.OPEN, bucketName=bucket)
        self.queue.put(op)
        self.cursor = next(self.reply).cursorID

    def read(self, op, k=None):
        op = Cursor(op=op, cursor=self.cursor, k=k)
        self.queue.put(op)
        return next(self.reply)
