# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote/kv.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from erigon.proto.types import types_pb2 as types_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fremote/kv.proto\x12\x06remote\x1a\x1bgoogle/protobuf/empty.proto\x1a\x11types/types.proto\"Z\n\x06\x43ursor\x12\x16\n\x02op\x18\x01 \x01(\x0e\x32\n.remote.Op\x12\x12\n\nbucketName\x18\x02 \x01(\t\x12\x0e\n\x06\x63ursor\x18\x03 \x01(\r\x12\t\n\x01k\x18\x04 \x01(\x0c\x12\t\n\x01v\x18\x05 \x01(\x0c\"<\n\x04Pair\x12\t\n\x01k\x18\x01 \x01(\x0c\x12\t\n\x01v\x18\x02 \x01(\x0c\x12\x10\n\x08\x63ursorID\x18\x03 \x01(\r\x12\x0c\n\x04txID\x18\x04 \x01(\x04\"<\n\rStorageChange\x12\x1d\n\x08location\x18\x01 \x01(\x0b\x32\x0b.types.H256\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xad\x01\n\rAccountChange\x12\x1c\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x0b.types.H160\x12\x13\n\x0bincarnation\x18\x02 \x01(\x04\x12\x1e\n\x06\x61\x63tion\x18\x03 \x01(\x0e\x32\x0e.remote.Action\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x12\x0c\n\x04\x63ode\x18\x05 \x01(\x0c\x12-\n\x0estorageChanges\x18\x06 \x03(\x0b\x32\x15.remote.StorageChange\"\x88\x01\n\x10StateChangeBatch\x12\x16\n\x0e\x64\x61tabaseViewID\x18\x01 \x01(\x04\x12(\n\x0b\x63hangeBatch\x18\x02 \x03(\x0b\x32\x13.remote.StateChange\x12\x1b\n\x13pendingBlockBaseFee\x18\x03 \x01(\x04\x12\x15\n\rblockGasLimit\x18\x04 \x01(\x04\"\x9d\x01\n\x0bStateChange\x12$\n\tdirection\x18\x01 \x01(\x0e\x32\x11.remote.Direction\x12\x13\n\x0b\x62lockHeight\x18\x02 \x01(\x04\x12\x1e\n\tblockHash\x18\x03 \x01(\x0b\x32\x0b.types.H256\x12&\n\x07\x63hanges\x18\x04 \x03(\x0b\x32\x15.remote.AccountChange\x12\x0b\n\x03txs\x18\x05 \x03(\x0c\"C\n\x12StateChangeRequest\x12\x13\n\x0bwithStorage\x18\x01 \x01(\x08\x12\x18\n\x10withTransactions\x18\x02 \x01(\x08\"\x12\n\x10SnapshotsRequest\"\x1f\n\x0eSnapshotsReply\x12\r\n\x05\x66iles\x18\x01 \x03(\t*\xfb\x01\n\x02Op\x12\t\n\x05\x46IRST\x10\x00\x12\r\n\tFIRST_DUP\x10\x01\x12\x08\n\x04SEEK\x10\x02\x12\r\n\tSEEK_BOTH\x10\x03\x12\x0b\n\x07\x43URRENT\x10\x04\x12\x08\n\x04LAST\x10\x06\x12\x0c\n\x08LAST_DUP\x10\x07\x12\x08\n\x04NEXT\x10\x08\x12\x0c\n\x08NEXT_DUP\x10\t\x12\x0f\n\x0bNEXT_NO_DUP\x10\x0b\x12\x08\n\x04PREV\x10\x0c\x12\x0c\n\x08PREV_DUP\x10\r\x12\x0f\n\x0bPREV_NO_DUP\x10\x0e\x12\x0e\n\nSEEK_EXACT\x10\x0f\x12\x13\n\x0fSEEK_BOTH_EXACT\x10\x10\x12\x08\n\x04OPEN\x10\x1e\x12\t\n\x05\x43LOSE\x10\x1f\x12\x11\n\rOPEN_DUP_SORT\x10 *H\n\x06\x41\x63tion\x12\x0b\n\x07STORAGE\x10\x00\x12\n\n\x06UPSERT\x10\x01\x12\x08\n\x04\x43ODE\x10\x02\x12\x0f\n\x0bUPSERT_CODE\x10\x03\x12\n\n\x06REMOVE\x10\x04*$\n\tDirection\x12\x0b\n\x07\x46ORWARD\x10\x00\x12\n\n\x06UNWIND\x10\x01\x32\xeb\x01\n\x02KV\x12\x36\n\x07Version\x12\x16.google.protobuf.Empty\x1a\x13.types.VersionReply\x12&\n\x02Tx\x12\x0e.remote.Cursor\x1a\x0c.remote.Pair(\x01\x30\x01\x12\x46\n\x0cStateChanges\x12\x1a.remote.StateChangeRequest\x1a\x18.remote.StateChangeBatch0\x01\x12=\n\tSnapshots\x12\x18.remote.SnapshotsRequest\x1a\x16.remote.SnapshotsReplyB\x11Z\x0f./remote;remoteb\x06proto3')

_OP = DESCRIPTOR.enum_types_by_name['Op']
Op = enum_type_wrapper.EnumTypeWrapper(_OP)
_ACTION = DESCRIPTOR.enum_types_by_name['Action']
Action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
_DIRECTION = DESCRIPTOR.enum_types_by_name['Direction']
Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
FIRST = 0
FIRST_DUP = 1
SEEK = 2
SEEK_BOTH = 3
CURRENT = 4
LAST = 6
LAST_DUP = 7
NEXT = 8
NEXT_DUP = 9
NEXT_NO_DUP = 11
PREV = 12
PREV_DUP = 13
PREV_NO_DUP = 14
SEEK_EXACT = 15
SEEK_BOTH_EXACT = 16
OPEN = 30
CLOSE = 31
OPEN_DUP_SORT = 32
STORAGE = 0
UPSERT = 1
CODE = 2
UPSERT_CODE = 3
REMOVE = 4
FORWARD = 0
UNWIND = 1


_CURSOR = DESCRIPTOR.message_types_by_name['Cursor']
_PAIR = DESCRIPTOR.message_types_by_name['Pair']
_STORAGECHANGE = DESCRIPTOR.message_types_by_name['StorageChange']
_ACCOUNTCHANGE = DESCRIPTOR.message_types_by_name['AccountChange']
_STATECHANGEBATCH = DESCRIPTOR.message_types_by_name['StateChangeBatch']
_STATECHANGE = DESCRIPTOR.message_types_by_name['StateChange']
_STATECHANGEREQUEST = DESCRIPTOR.message_types_by_name['StateChangeRequest']
_SNAPSHOTSREQUEST = DESCRIPTOR.message_types_by_name['SnapshotsRequest']
_SNAPSHOTSREPLY = DESCRIPTOR.message_types_by_name['SnapshotsReply']
Cursor = _reflection.GeneratedProtocolMessageType('Cursor', (_message.Message,), {
  'DESCRIPTOR' : _CURSOR,
  '__module__' : 'remote.kv_pb2'
  # @@protoc_insertion_point(class_scope:remote.Cursor)
  })
_sym_db.RegisterMessage(Cursor)

Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), {
  'DESCRIPTOR' : _PAIR,
  '__module__' : 'remote.kv_pb2'
  # @@protoc_insertion_point(class_scope:remote.Pair)
  })
_sym_db.RegisterMessage(Pair)

StorageChange = _reflection.GeneratedProtocolMessageType('StorageChange', (_message.Message,), {
  'DESCRIPTOR' : _STORAGECHANGE,
  '__module__' : 'remote.kv_pb2'
  # @@protoc_insertion_point(class_scope:remote.StorageChange)
  })
_sym_db.RegisterMessage(StorageChange)

AccountChange = _reflection.GeneratedProtocolMessageType('AccountChange', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTCHANGE,
  '__module__' : 'remote.kv_pb2'
  # @@protoc_insertion_point(class_scope:remote.AccountChange)
  })
_sym_db.RegisterMessage(AccountChange)

StateChangeBatch = _reflection.GeneratedProtocolMessageType('StateChangeBatch', (_message.Message,), {
  'DESCRIPTOR' : _STATECHANGEBATCH,
  '__module__' : 'remote.kv_pb2'
  # @@protoc_insertion_point(class_scope:remote.StateChangeBatch)
  })
_sym_db.RegisterMessage(StateChangeBatch)

StateChange = _reflection.GeneratedProtocolMessageType('StateChange', (_message.Message,), {
  'DESCRIPTOR' : _STATECHANGE,
  '__module__' : 'remote.kv_pb2'
  # @@protoc_insertion_point(class_scope:remote.StateChange)
  })
_sym_db.RegisterMessage(StateChange)

StateChangeRequest = _reflection.GeneratedProtocolMessageType('StateChangeRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATECHANGEREQUEST,
  '__module__' : 'remote.kv_pb2'
  # @@protoc_insertion_point(class_scope:remote.StateChangeRequest)
  })
_sym_db.RegisterMessage(StateChangeRequest)

SnapshotsRequest = _reflection.GeneratedProtocolMessageType('SnapshotsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTSREQUEST,
  '__module__' : 'remote.kv_pb2'
  # @@protoc_insertion_point(class_scope:remote.SnapshotsRequest)
  })
_sym_db.RegisterMessage(SnapshotsRequest)

SnapshotsReply = _reflection.GeneratedProtocolMessageType('SnapshotsReply', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTSREPLY,
  '__module__' : 'remote.kv_pb2'
  # @@protoc_insertion_point(class_scope:remote.SnapshotsReply)
  })
_sym_db.RegisterMessage(SnapshotsReply)

_KV = DESCRIPTOR.services_by_name['KV']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\017./remote;remote'
  _OP._serialized_start=889
  _OP._serialized_end=1140
  _ACTION._serialized_start=1142
  _ACTION._serialized_end=1214
  _DIRECTION._serialized_start=1216
  _DIRECTION._serialized_end=1252
  _CURSOR._serialized_start=75
  _CURSOR._serialized_end=165
  _PAIR._serialized_start=167
  _PAIR._serialized_end=227
  _STORAGECHANGE._serialized_start=229
  _STORAGECHANGE._serialized_end=289
  _ACCOUNTCHANGE._serialized_start=292
  _ACCOUNTCHANGE._serialized_end=465
  _STATECHANGEBATCH._serialized_start=468
  _STATECHANGEBATCH._serialized_end=604
  _STATECHANGE._serialized_start=607
  _STATECHANGE._serialized_end=764
  _STATECHANGEREQUEST._serialized_start=766
  _STATECHANGEREQUEST._serialized_end=833
  _SNAPSHOTSREQUEST._serialized_start=835
  _SNAPSHOTSREQUEST._serialized_end=853
  _SNAPSHOTSREPLY._serialized_start=855
  _SNAPSHOTSREPLY._serialized_end=886
  _KV._serialized_start=1255
  _KV._serialized_end=1490
# @@protoc_insertion_point(module_scope)