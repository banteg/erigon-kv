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
    else:
        return rlp.decode(data, sedes=LondonTypedTransaction)._inner
