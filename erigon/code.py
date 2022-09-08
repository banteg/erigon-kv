from erigon.kv import ErigonKV, Op
from time import perf_counter
from datetime import timedelta
from humanize import naturalsize


def main():
    start = perf_counter()
    hit_end = False
    found = 0
    size = 0
    kv = ErigonKV()
    kv.open("Code")

    while True:
        batch = [kv.read(Op.NEXT) for _ in range(1000)]
        for code in batch:
            if code.k == b"":
                hit_end = True
                break
            found += 1
            size += len(code.v)

        pos = int.from_bytes(code.k, "big") / 2**256
        elapsed = timedelta(seconds=perf_counter() - start)
        print(f"\r{pos:5.3%} {code.k[:8].hex()} [{found} codes, {naturalsize(size)}] {elapsed}", end="", flush=True)
        if hit_end:
            print()
            break


if __name__ == "__main__":
    main()
