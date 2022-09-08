# erigon uses an accursed encoding for hash types
# ported from https://github.com/ledgerwatch/erigon-lib/blob/main/gointerfaces/type_utils.go
from erigon.proto.types.types_pb2 import H128, H160, H256, H512, H1024, H2048


def b(number: int, size: int = 8):
    return number.to_bytes(size, "big")


def i(data: bytes):
    return int.from_bytes(data, "big")


def decode(msg):
    match msg:
        case H128():
            return b(msg.hi) + b(msg.lo)
        case H160():
            return decode(msg.hi) + b(msg.lo, 4)
        case H256() | H512() | H1024() | H2048():
            return decode(msg.hi) + decode(msg.lo)

    raise TypeError("unsupported type %s", type(msg))


def encode(data: bytes):
    match len(data):
        case 16:
            return H128(hi=i(data[:8]), lo=i(data[8:16]))
        case 20:
            return H160(hi=encode(data[:16]), lo=i(data[16:20]))
        case 32:
            return H256(hi=encode(data[:16]), lo=encode(data[16:32]))
        case 64:
            return H512(hi=encode(data[:32]), lo=encode(data[32:]))
        case 128:
            return H1024(hi=encode(data[:64]), lo=encode(data[64:128]))
        case 256:
            return H2048(hi=encode(data[:128]), lo=encode(data[128:256]))

    raise ValueError("invalid data length %d", len(data))
