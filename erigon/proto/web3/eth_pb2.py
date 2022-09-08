# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: web3/eth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from erigon.proto.web3 import common_pb2 as web3_dot_common__pb2
from erigon.proto.types import types_pb2 as types_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eweb3/eth.proto\x12\x04web3\x1a\x1bgoogle/protobuf/empty.proto\x1a\x11web3/common.proto\x1a\x11types/types.proto\"+\n\x13\x42lockNumberResponse\x12\x14\n\x0c\x62lock_number\x18\x01 \x01(\x04\"/\n\x17ResolveBlockHashRequest\x12\x14\n\x0c\x62lock_number\x18\x01 \x01(\x04\"O\n\x18ResolveBlockHashResponse\x12$\n\nblock_hash\x18\x01 \x01(\x0b\x32\x0b.types.H256H\x00\x88\x01\x01\x42\r\n\x0b_block_hash\"O\n\x0c\x42lockRequest\x12+\n\x0fsearch_location\x18\x01 \x01(\x0b\x32\r.web3.BlockIdH\x00\x88\x01\x01\x42\x12\n\x10_search_location\"D\n\x12LightBlockResponse\x12$\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x10.web3.LightBlockH\x00\x88\x01\x01\x42\x08\n\x06_block\"B\n\x11\x46ullBlockResponse\x12#\n\x05\x62lock\x18\x01 \x01(\x0b\x32\x0f.web3.FullBlockH\x00\x88\x01\x01\x42\x08\n\x06_block\"X\n\x13TransactionResponse\x12\x31\n\x0btransaction\x18\x01 \x01(\x0b\x32\x17.web3.StoredTransactionH\x00\x88\x01\x01\x42\x0e\n\x0c_transaction2\x8e\x03\n\x06\x45thApi\x12@\n\x0b\x42lockNumber\x12\x16.google.protobuf.Empty\x1a\x19.web3.BlockNumberResponse\x12Q\n\x10ResolveBlockHash\x12\x1d.web3.ResolveBlockHashRequest\x1a\x1e.web3.ResolveBlockHashResponse\x12:\n\nLightBlock\x12\x12.web3.BlockRequest\x1a\x18.web3.LightBlockResponse\x12\x38\n\tFullBlock\x12\x12.web3.BlockRequest\x1a\x17.web3.FullBlockResponse\x12;\n\x11TransactionByHash\x12\x0b.types.H256\x1a\x19.web3.TransactionResponse\x12<\n\x0fSendTransaction\x12\x11.web3.Transaction\x1a\x16.google.protobuf.Emptyb\x06proto3')



_BLOCKNUMBERRESPONSE = DESCRIPTOR.message_types_by_name['BlockNumberResponse']
_RESOLVEBLOCKHASHREQUEST = DESCRIPTOR.message_types_by_name['ResolveBlockHashRequest']
_RESOLVEBLOCKHASHRESPONSE = DESCRIPTOR.message_types_by_name['ResolveBlockHashResponse']
_BLOCKREQUEST = DESCRIPTOR.message_types_by_name['BlockRequest']
_LIGHTBLOCKRESPONSE = DESCRIPTOR.message_types_by_name['LightBlockResponse']
_FULLBLOCKRESPONSE = DESCRIPTOR.message_types_by_name['FullBlockResponse']
_TRANSACTIONRESPONSE = DESCRIPTOR.message_types_by_name['TransactionResponse']
BlockNumberResponse = _reflection.GeneratedProtocolMessageType('BlockNumberResponse', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKNUMBERRESPONSE,
  '__module__' : 'web3.eth_pb2'
  # @@protoc_insertion_point(class_scope:web3.BlockNumberResponse)
  })
_sym_db.RegisterMessage(BlockNumberResponse)

ResolveBlockHashRequest = _reflection.GeneratedProtocolMessageType('ResolveBlockHashRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOLVEBLOCKHASHREQUEST,
  '__module__' : 'web3.eth_pb2'
  # @@protoc_insertion_point(class_scope:web3.ResolveBlockHashRequest)
  })
_sym_db.RegisterMessage(ResolveBlockHashRequest)

ResolveBlockHashResponse = _reflection.GeneratedProtocolMessageType('ResolveBlockHashResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESOLVEBLOCKHASHRESPONSE,
  '__module__' : 'web3.eth_pb2'
  # @@protoc_insertion_point(class_scope:web3.ResolveBlockHashResponse)
  })
_sym_db.RegisterMessage(ResolveBlockHashResponse)

BlockRequest = _reflection.GeneratedProtocolMessageType('BlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKREQUEST,
  '__module__' : 'web3.eth_pb2'
  # @@protoc_insertion_point(class_scope:web3.BlockRequest)
  })
_sym_db.RegisterMessage(BlockRequest)

LightBlockResponse = _reflection.GeneratedProtocolMessageType('LightBlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _LIGHTBLOCKRESPONSE,
  '__module__' : 'web3.eth_pb2'
  # @@protoc_insertion_point(class_scope:web3.LightBlockResponse)
  })
_sym_db.RegisterMessage(LightBlockResponse)

FullBlockResponse = _reflection.GeneratedProtocolMessageType('FullBlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _FULLBLOCKRESPONSE,
  '__module__' : 'web3.eth_pb2'
  # @@protoc_insertion_point(class_scope:web3.FullBlockResponse)
  })
_sym_db.RegisterMessage(FullBlockResponse)

TransactionResponse = _reflection.GeneratedProtocolMessageType('TransactionResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTIONRESPONSE,
  '__module__' : 'web3.eth_pb2'
  # @@protoc_insertion_point(class_scope:web3.TransactionResponse)
  })
_sym_db.RegisterMessage(TransactionResponse)

_ETHAPI = DESCRIPTOR.services_by_name['EthApi']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BLOCKNUMBERRESPONSE._serialized_start=91
  _BLOCKNUMBERRESPONSE._serialized_end=134
  _RESOLVEBLOCKHASHREQUEST._serialized_start=136
  _RESOLVEBLOCKHASHREQUEST._serialized_end=183
  _RESOLVEBLOCKHASHRESPONSE._serialized_start=185
  _RESOLVEBLOCKHASHRESPONSE._serialized_end=264
  _BLOCKREQUEST._serialized_start=266
  _BLOCKREQUEST._serialized_end=345
  _LIGHTBLOCKRESPONSE._serialized_start=347
  _LIGHTBLOCKRESPONSE._serialized_end=415
  _FULLBLOCKRESPONSE._serialized_start=417
  _FULLBLOCKRESPONSE._serialized_end=483
  _TRANSACTIONRESPONSE._serialized_start=485
  _TRANSACTIONRESPONSE._serialized_end=573
  _ETHAPI._serialized_start=576
  _ETHAPI._serialized_end=974
# @@protoc_insertion_point(module_scope)