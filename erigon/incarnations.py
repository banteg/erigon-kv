from eth_utils import keccak, to_canonical_address, to_int
from typer import Typer

from erigon.kv import ErigonKV, Op

app = Typer()


@app.command()
def incarnations(address: str):
    kv = ErigonKV()
    canonical_address: bytes = to_canonical_address(address)

    # read number of incarnations
    kv.open("IncarnationMap")
    read = kv.read(Op.SEEK_EXACT, canonical_address)
    assert read.k[-20:] == canonical_address, "could not find address"
    num_incarnations = to_int(read.v)
    print(f"{num_incarnations} incarnations")

    # read code hashes
    kv.open("HashedCodeHash")
    code_hashes = [kv.read(Op.SEEK_EXACT, keccak(canonical_address) + read.v)]
    code_hashes += [kv.read(Op.PREV) for _ in range(num_incarnations - 1)]

    # read codes
    kv.open("Code")
    codes = {
        int.from_bytes(item.k[-8:], "big"): kv.read(Op.SEEK_EXACT, k=item.v).v.hex()
        for item in reversed(code_hashes)
    }

    return codes


if __name__ == "__main__":
    app()
