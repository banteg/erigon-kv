import rlp
from eth.vm.forks.berlin.transactions import AccessListTransaction
from eth.vm.forks.london.transactions import (
    DynamicFeeTransaction,
    LondonLegacyTransaction,
    LondonTypedTransaction,
)

Transaction = LondonLegacyTransaction | AccessListTransaction | DynamicFeeTransaction


def decode_transaction(data: bytes) -> Transaction:
    # an rlp list indicates a legacy transaction
    if data[0] >= 0xC0:
        return rlp.decode(data, sedes=LondonLegacyTransaction)

    # there could be a header which contains encodes the payload size
    if data[0] >= 0xB7:
        # len_of_len = data[0] - 0xb7
        # len_of_data = to_int(data[1:1+len_of_len])
        offset = data[0] - 0xB7 + 1
        data = data[offset:]

    return LondonTypedTransaction.decode(data)._inner
