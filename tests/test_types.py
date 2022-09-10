import pytest
from erigon.proto.types.types_pb2 import H128, H160, H256, H512, H1024, H2048
from erigon.types import decode_hash, encode_hash

data = {
    "h128_1": {"enc": H128(hi=1, lo=2), "dec": "00000000000000010000000000000002"},
    "h128_2": {"enc": H128(hi=3, lo=4), "dec": "00000000000000030000000000000004"},
}
data["h160"] = {
    "enc": H160(hi=data["h128_1"]["enc"], lo=5),
    "dec": data["h128_1"]["dec"] + "00000005",
}
data["h256_1"] = {
    "enc": H256(hi=data["h128_1"]["enc"], lo=data["h128_2"]["enc"]),
    "dec": data["h128_1"]["dec"] + data["h128_2"]["dec"],
}
data["h256_2"] = {
    "enc": H256(hi=data["h128_2"]["enc"], lo=data["h128_1"]["enc"]),
    "dec": data["h128_2"]["dec"] + data["h128_1"]["dec"],
}
data["h512_1"] = {
    "enc": H512(hi=data["h256_1"]["enc"], lo=data["h256_2"]["enc"]),
    "dec": data["h256_1"]["dec"] + data["h256_2"]["dec"],
}
data["h512_2"] = {
    "enc": H512(hi=data["h256_2"]["enc"], lo=data["h256_1"]["enc"]),
    "dec": data["h256_2"]["dec"] + data["h256_1"]["dec"],
}
data["h1024_1"] = {
    "enc": H1024(hi=data["h512_1"]["enc"], lo=data["h512_2"]["enc"]),
    "dec": data["h512_1"]["dec"] + data["h512_2"]["dec"],
}
data["h1024_2"] = {
    "enc": H1024(hi=data["h512_2"]["enc"], lo=data["h512_1"]["enc"]),
    "dec": data["h512_2"]["dec"] + data["h512_1"]["dec"],
}
data["h2048"] = {
    "enc": H2048(hi=data["h1024_1"]["enc"], lo=data["h1024_2"]["enc"]),
    "dec": data["h1024_1"]["dec"] + data["h1024_2"]["dec"],
}


@pytest.mark.parametrize("key", data)
def test_decode(key):
    assert decode_hash(data[key]["enc"]) == bytes.fromhex(data[key]["dec"])


@pytest.mark.parametrize("key", data)
def test_encode(key):
    assert encode_hash(bytes.fromhex(data[key]["dec"])) == data[key]["enc"]
