# read erigon snapshot format

# indexes (idx), segments (seg)
import itertools
from typer import Typer
import os
import mmap
from devtools import debug
from msgspec import Struct

app = Typer()


def to_int(b: bytes) -> int:
    return int.from_bytes(b, "big")


def uvarint(stream):
    """Read a varint from `stream`"""
    shift = 0
    result = 0
    for offset in itertools.count():
        i = stream[offset]
        result |= (i & 0x7F) << shift
        shift += 7
        if not (i & 0x80):
            break

    return result, offset + 1


class Codeword(Struct):
    code: int  # code associated with that word
    length: int  # Number of bits in the codes
    pattern: bytes  # Pattern corresponding to entries
    ptr: object  # pointer to deeper level tables
    nxt: bytes  # points to next word in condensed table


def new_pattern_table(bit_len):
    ...


@app.command()
def read_seg(path: str):
    descriptor = os.open(path, os.O_RDONLY)
    reader = mmap.mmap(descriptor, 0, access=mmap.ACCESS_READ)

    words_count = to_int(reader[:8])
    empty_words_count = to_int(reader[8:16])
    dict_size = to_int(reader[16:24])
    data = reader[24 : 24 + dict_size]
    debug(words_count, empty_words_count, dict_size)

    depths = []
    patterns = []
    pattern_max_depth = 0
    i = 0

    while i < dict_size:
        d, ns = uvarint(data[i:])
        if d > 2048:
            raise ValueError("dictionary is invalid: patternMaxDepth=%d", d)
        depths.append(d)
        if d > pattern_max_depth:
            pattern_max_depth = d
        i += ns
        l, n = uvarint(data[i:])
        i += n
        patterns.append(data[i : i + l])
        # debug(d, l, n, data[i : i + l])
        i += l

    if dict_size > 0:
        bit_len = min(pattern_max_depth, 9)
        pattern_table = new_pattern_table(bit_len)


if __name__ == "__main__":
    app()
