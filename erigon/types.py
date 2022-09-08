# erigon uses an accursed encoding for hash types
# ported from https://github.com/ledgerwatch/erigon-lib/blob/main/gointerfaces/type_utils.go
from erigon.proto.types.types_pb2 import H128, H160, H256, H512, H1024, H2048


def b(number: int, size: int = 8):
    return number.to_bytes(size, "big")


def i(data: bytes):
    return int.from_bytes(data, "big")


def decode(msg):
    if isinstance(msg, H128):
        return b(msg.hi) + b(msg.lo)
    elif isinstance(msg, H160):
        return decode(msg.hi) + b(msg.lo, 4)
    elif isinstance(msg, (H256, H512, H1024, H2048)):
        return decode(msg.hi) + decode(msg.lo)
