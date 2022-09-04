import itertools
from collections import Counter

import cbor
from erigon.kv import ErigonKV, Op
from erigon.accounts import Account
from rich import box
from rich.live import Live
from rich.table import Table
from rich.progress import track, Progress
from typer import Typer
from rich.console import Console, Group

app = Typer()

PREFIXES = {
    "6004361015": ("vyper", "0.2.0-0.2.4,0.2.11-0.3.3"),
    "341561000a": ("vyper", "0.2.5-0.2.8"),
    "6080604052": ("solc", "0.4.22+"),
    "6060604052": ("solc", "0.4.11-0.4.21"),
    "363d3d373d3d3d363d73": ("proxy", "minimal"),
    "366000600037611000600036600073": ("proxy", "vyper"),
}


def detect_compiler(code):
    # read cbor-encoded version from solidity 0.6.0+
    # https://docs.soliditylang.org/en/v0.8.13/metadata.html#encoding-of-the-metadata-hash-in-the-bytecode
    if code[-53:-51] == b"\xa2\x64":
        try:
            data = cbor.loads(code[-53:])
            version = tuple(data["solc"])
            return "solc", version
        except (RuntimeError, KeyError):
            pass

    # read cbor-encoded version from vyper 0.3.4+
    # https://github.com/vyperlang/vyper/blob/b096dbdc9d1d61e7d34d7ed2e4107234951b982b/vyper/ir/compile_ir.py#L996
    if code[-13:-11] == b"\xa1\x65":
        try:
            data = cbor.loads(code[-13:])
            version = tuple(data["vyper"])
            return "vyper", version
        except (RuntimeError, KeyError):
            pass

    # guess from bytecode prefix
    for prefix in PREFIXES:
        if code.startswith(bytes.fromhex(prefix)):
            return PREFIXES[prefix]


def generate_table(data) -> Table:
    """Make a new table."""
    total = sum(data.values())
    table = Table(box=box.SIMPLE, show_footer=True)
    table.add_column("compiler")
    table.add_column("version")
    table.add_column("contracts", footer=f"{total}")
    table.add_column("percent")
    colors = {
        "solc": "red",
        "vyper": "green",
        "proxy": "cyan",
        "eoa": "yellow",
        "unknown": "dim",
    }

    for key, value in data.most_common():
        if key is None:
            compiler, version = "[dim]--", "[dim]--"
        else:
            compiler, version = key
            compiler = f"[{colors[compiler]}]{compiler}"
            if isinstance(version, tuple):
                version = ".".join(map(str, version))
        table.add_row(f"{compiler}", f"{version}", f"{value}", f"{value / total:.3%}")

    return table


@app.command()
def compilers():
    kv = ErigonKV()
    kv.open("Code")
    compiler_counts = Counter()

    with Live() as live:
        for i in itertools.count(1):
            # print(i)
            row = kv.read(Op.NEXT)
            if row.k == b"":
                live.update(generate_table(compiler_counts))
                break
            compiler = detect_compiler(row.v)
            compiler_counts[compiler] += 1
            if i % 1000 == 0:
                live.update(generate_table(compiler_counts))


@app.command()
def accounts():
    console = Console()
    bar = Progress(console=console)
    code_task = bar.add_task("code")
    acc_task = bar.add_task("accounts")

    with Live(console=console) as live:
        compiler_counts = Counter()
        codehash_to_compiler = {}
        kv = ErigonKV()
        kv.open("Code")
        for i in itertools.count(1):
            row = kv.read(Op.NEXT)
            if row.k == b"":
                break
            compiler = detect_compiler(row.v)
            codehash_to_compiler[row.k] = compiler
            compiler_counts[compiler] += 1
            if i % 10000 == 0:
                progress = int.from_bytes(row.k, "big") / 2**256
                bar.update(code_task, completed=progress * 100)
                table = generate_table(compiler_counts)
                live.update(Group(bar, table), refresh=True)

        account_counts: Counter = Counter()
        kv.open("PlainState", dup_sort=True)
        key = bytes(20)

        for i in itertools.count(1):
            row = kv.read(Op.SEEK, k=key)
            if row.k == b"":
                live.update(generate_table(account_counts))
                print("end")
                break

            if len(row.k) == 20:
                acc: Account = Account.from_storage(row.k.hex(), row.v)
                if acc.code_hash:
                    compiler = codehash_to_compiler.get(acc.code_hash) or ("unknown", "")
                    account_counts[compiler] += 1

            if i % 10000 == 0:
                # console.log(row.k.hex())
                progress = int.from_bytes(row.k[:20], "big") / 2**160
                bar.update(acc_task, completed=round(progress * 100, 3))
                table = generate_table(account_counts)
                live.update(Group(bar, table), refresh=True)

            # increment 20th byte and find the next address
            key = int.to_bytes(int.from_bytes(row.k[:20], "big") + 1, 20, "big")


if __name__ == "__main__":
    app()
