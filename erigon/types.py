# erigon uses an accursed encoding for hash types
# ported from https://github.com/ledgerwatch/erigon-lib/blob/main/gointerfaces/type_utils.go
from erigon.proto.types.types_pb2 import H128, H160, H256, H512, H1024, H2048


def to_bytes(number: int, size: int = 8):
    return number.to_bytes(size, "big")


def to_int(data: bytes):
    return int.from_bytes(data, "big")


def decode(msg):
    match msg:
        case H128():
            return to_bytes(msg.hi) + to_bytes(msg.lo)
        case H160():
            return decode(msg.hi) + to_bytes(msg.lo, 4)
        case H256() | H512() | H1024() | H2048():
            return decode(msg.hi) + decode(msg.lo)

    raise TypeError("unsupported type %s", type(msg))


def encode(data: bytes):
    match len(data):
        case 16:
            return H128(hi=to_int(data[:8]), lo=to_int(data[8:]))
        case 20:
            return H160(hi=encode(data[:16]), lo=to_int(data[16:20]))
        case 32:
            return H256(hi=encode(data[:16]), lo=encode(data[16:32]))
        case 64:
            return H512(hi=encode(data[:32]), lo=encode(data[32:]))
        case 128:
            return H1024(hi=encode(data[:64]), lo=encode(data[64:]))
        case 256:
            return H2048(hi=encode(data[:128]), lo=encode(data[128:]))

    raise ValueError("invalid data length %d", len(data))
