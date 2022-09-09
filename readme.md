# erigon-kv

get direct access to erigon database over grpc api.

## low-level api

this interface wraps the [kv api](https://github.com/ledgerwatch/interfaces/blob/master/remote/kv.proto) and allows you to read and iterate over any table.

```python
from erigon.kv import ErigonKV

kv = ErigonKV()
await kv.connect()

async with kv.open('Code') as cursor:
    await cursor.seek(b'\xff\xff')

    async for row in cursor:
        print(row)
```

`ErigonKV.connect` connects to the private api (default: `127.0.0.1:9090`) and opens a read transaction. a transaction offers a consistent view over the database, but be wary of long-running transactions, as they can impact the database performance.

`ErigonKV.open` returns an `ErigonCursor` object which supports async iteration and seeking. it will also automatically close the cursor when you are finished.

you can also open a table in a dup sort mode, in which a key can have more than one value associated. this mode is utilized in the `PlainState` table for contract storage.

`ErigonCursor` supports `seek`, `seek_exact`, `first`, `last`, `prev` methods, as well as iteration. there is also a `read` method which you can use with rarer ops.

the cursor starts at the first row by default, so you can just iterate over it.

not all tables use an intuitive layout, read the [annotated source](https://github.com/ledgerwatch/erigon-lib/blob/main/kv/tables.go) for a description of the key and value structure of each bucket.

## high-level api

this interface provides common shortcuts to read block headers, accounts, and to enumerate account storage.
