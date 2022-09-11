from erigon.types import Account, decode_account


def test_account():
    # fmt: off
    data = bytes.fromhex('0f0101074e96eef7886cf6010120aea7d4252f6245f301e540cfbee27d3a88de543af8e49c5c62405d5499fab7e5')
    code_hash = bytes.fromhex('aea7d4252f6245f301e540cfbee27d3a88de543af8e49c5c62405d5499fab7e5')
    # fmt: on
    account = decode_account(data)
    assert account == Account(
        nonce=1,
        balance=22121001282727158,
        incarnation=1,
        code_hash=code_hash,
    )
