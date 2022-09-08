# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: web3/trace.proto
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
from erigon.proto.web3 import common_pb2 as web3_dot_common__pb2
from erigon.proto.types import types_pb2 as types_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10web3/trace.proto\x12\x04web3\x1a\x1bgoogle/protobuf/empty.proto\x1a\x11web3/common.proto\x1a\x11types/types.proto\"\xef\x01\n\nLegacyCall\x12\x1e\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x0b.types.H160H\x00\x88\x01\x01\x12\x1c\n\x02to\x18\x02 \x01(\x0b\x32\x0b.types.H160H\x01\x88\x01\x01\x12\x16\n\tgas_limit\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x16\n\tgas_price\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x1f\n\x05value\x18\x05 \x01(\x0b\x32\x0b.types.H256H\x04\x88\x01\x01\x12\x12\n\x05input\x18\x06 \x01(\x0cH\x05\x88\x01\x01\x42\x07\n\x05_fromB\x05\n\x03_toB\x0c\n\n_gas_limitB\x0c\n\n_gas_priceB\x08\n\x06_valueB\x08\n\x06_input\"7\n\nAccessList\x12)\n\x0b\x61\x63\x63\x65ss_list\x18\x01 \x03(\x0b\x32\x14.web3.AccessListItem\"\xac\x02\n\x0b\x45IP2930Call\x12\x1e\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x0b.types.H160H\x00\x88\x01\x01\x12\x1c\n\x02to\x18\x02 \x01(\x0b\x32\x0b.types.H160H\x01\x88\x01\x01\x12\x16\n\tgas_limit\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12\x16\n\tgas_price\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x1f\n\x05value\x18\x05 \x01(\x0b\x32\x0b.types.H256H\x04\x88\x01\x01\x12\x12\n\x05input\x18\x06 \x01(\x0cH\x05\x88\x01\x01\x12*\n\x0b\x61\x63\x63\x65ss_list\x18\x07 \x01(\x0b\x32\x10.web3.AccessListH\x06\x88\x01\x01\x42\x07\n\x05_fromB\x05\n\x03_toB\x0c\n\n_gas_limitB\x0c\n\n_gas_priceB\x08\n\x06_valueB\x08\n\x06_inputB\x0e\n\x0c_access_list\"\xfc\x02\n\x0b\x45IP1559Call\x12\x1e\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x0b.types.H160H\x00\x88\x01\x01\x12\x1c\n\x02to\x18\x02 \x01(\x0b\x32\x0b.types.H160H\x01\x88\x01\x01\x12\x16\n\tgas_limit\x18\x03 \x01(\x04H\x02\x88\x01\x01\x12%\n\x18max_priority_fee_per_gas\x18\x04 \x01(\x04H\x03\x88\x01\x01\x12\x1c\n\x0fmax_fee_per_gas\x18\x05 \x01(\x04H\x04\x88\x01\x01\x12\x1f\n\x05value\x18\x06 \x01(\x0b\x32\x0b.types.H256H\x05\x88\x01\x01\x12\x12\n\x05input\x18\x07 \x01(\x0cH\x06\x88\x01\x01\x12*\n\x0b\x61\x63\x63\x65ss_list\x18\x08 \x01(\x0b\x32\x10.web3.AccessListH\x07\x88\x01\x01\x42\x07\n\x05_fromB\x05\n\x03_toB\x0c\n\n_gas_limitB\x1b\n\x19_max_priority_fee_per_gasB\x12\n\x10_max_fee_per_gasB\x08\n\x06_valueB\x08\n\x06_inputB\x0e\n\x0c_access_list\"~\n\x04\x43\x61ll\x12\"\n\x06legacy\x18\x01 \x01(\x0b\x32\x10.web3.LegacyCallH\x00\x12$\n\x07\x65ip2930\x18\x02 \x01(\x0b\x32\x11.web3.EIP2930CallH\x00\x12$\n\x07\x65ip1559\x18\x03 \x01(\x0b\x32\x11.web3.EIP1559CallH\x00\x42\x06\n\x04\x63\x61ll\"A\n\nTraceKinds\x12\r\n\x05trace\x18\x01 \x01(\x08\x12\x10\n\x08vm_trace\x18\x02 \x01(\x08\x12\x12\n\nstate_diff\x18\x03 \x01(\x08\"H\n\x0b\x43\x61llRequest\x12\x18\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\n.web3.Call\x12\x1f\n\x05kinds\x18\x02 \x01(\x0b\x32\x10.web3.TraceKinds\"Q\n\x0c\x43\x61llRequests\x12 \n\x05\x63\x61lls\x18\x01 \x03(\x0b\x32\x11.web3.CallRequest\x12\x1f\n\x08\x62lock_id\x18\x02 \x01(\x0b\x32\r.web3.BlockId\"O\n\x11TraceBlockRequest\x12\x19\n\x02id\x18\x01 \x01(\x0b\x32\r.web3.BlockId\x12\x1f\n\x05kinds\x18\x02 \x01(\x0b\x32\x10.web3.TraceKinds\"U\n\x17TraceTransactionRequest\x12\x19\n\x04hash\x18\x01 \x01(\x0b\x32\x0b.types.H256\x12\x1f\n\x05kinds\x18\x02 \x01(\x0b\x32\x10.web3.TraceKinds\",\n\nAddressSet\x12\x1e\n\taddresses\x18\x01 \x03(\x0b\x32\x0b.types.H160\"\xa7\x02\n\rFilterRequest\x12&\n\nfrom_block\x18\x01 \x01(\x0b\x32\r.web3.BlockIdH\x00\x88\x01\x01\x12$\n\x08to_block\x18\x02 \x01(\x0b\x32\r.web3.BlockIdH\x01\x88\x01\x01\x12-\n\x0e\x66rom_addresses\x18\x03 \x01(\x0b\x32\x10.web3.AddressSetH\x02\x88\x01\x01\x12+\n\x0cto_addresses\x18\x04 \x01(\x0b\x32\x10.web3.AddressSetH\x03\x88\x01\x01\x12#\n\x04mode\x18\x05 \x01(\x0e\x32\x10.web3.FilterModeH\x04\x88\x01\x01\x42\r\n\x0b_from_blockB\x0b\n\t_to_blockB\x11\n\x0f_from_addressesB\x0f\n\r_to_addressesB\x07\n\x05_mode\"\xae\x01\n\nCallAction\x12\x19\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x0b.types.H160\x12\x17\n\x02to\x18\x02 \x01(\x0b\x32\x0b.types.H160\x12\x1a\n\x05value\x18\x03 \x01(\x0b\x32\x0b.types.H256\x12\x0b\n\x03gas\x18\x04 \x01(\x04\x12\r\n\x05input\x18\x05 \x01(\x0c\x12&\n\tcall_type\x18\x06 \x01(\x0e\x32\x0e.web3.CallTypeH\x00\x88\x01\x01\x42\x0c\n\n_call_type\"`\n\x0c\x43reateAction\x12\x19\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x0b.types.H160\x12\x1a\n\x05value\x18\x02 \x01(\x0b\x32\x0b.types.H256\x12\x0b\n\x03gas\x18\x03 \x01(\x04\x12\x0c\n\x04init\x18\x04 \x01(\x0c\"u\n\x12SelfdestructAction\x12\x1c\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x0b.types.H160\x12#\n\x0erefund_address\x18\x02 \x01(\x0b\x32\x0b.types.H160\x12\x1c\n\x07\x62\x61lance\x18\x03 \x01(\x0b\x32\x0b.types.H256\"\x9f\x01\n\x0cRewardAction\x12\x1b\n\x06\x61uthor\x18\x01 \x01(\x0b\x32\x0b.types.H160\x12\x1a\n\x05value\x18\x02 \x01(\x0b\x32\x0b.types.H256\x12\x32\n\x0breward_type\x18\x03 \x01(\x0e\x32\x1d.web3.RewardAction.RewardType\"\"\n\nRewardType\x12\t\n\x05\x42lock\x10\x00\x12\t\n\x05Uncle\x10\x01\"\xb2\x01\n\x06\x41\x63tion\x12 \n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x10.web3.CallActionH\x00\x12$\n\x06\x63reate\x18\x02 \x01(\x0b\x32\x12.web3.CreateActionH\x00\x12\x30\n\x0cselfdestruct\x18\x03 \x01(\x0b\x32\x18.web3.SelfdestructActionH\x00\x12$\n\x06reward\x18\x04 \x01(\x0b\x32\x12.web3.RewardActionH\x00\x42\x08\n\x06\x61\x63tion\"\x82\x01\n\x05Trace\x12\x1c\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32\x0c.web3.Action\x12&\n\x06result\x18\x02 \x01(\x0b\x32\x11.web3.TraceResultH\x00\x88\x01\x01\x12\x11\n\tsubtraces\x18\x03 \x01(\x04\x12\x15\n\rtrace_address\x18\x04 \x03(\x04\x42\t\n\x07_result\".\n\nCallOutput\x12\x10\n\x08gas_used\x18\x01 \x01(\x04\x12\x0e\n\x06output\x18\x02 \x01(\x0c\"L\n\x0c\x43reateOutput\x12\x10\n\x08gas_used\x18\x01 \x01(\x04\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x0c\x12\x1c\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x0b.types.H160\"_\n\x0bTraceOutput\x12 \n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x10.web3.CallOutputH\x00\x12$\n\x06\x63reate\x18\x02 \x01(\x0b\x32\x12.web3.CreateOutputH\x00\x42\x08\n\x06output\"M\n\x0bTraceResult\x12#\n\x06output\x18\x01 \x01(\x0b\x32\x11.web3.TraceOutputH\x00\x12\x0f\n\x05\x65rror\x18\x02 \x01(\tH\x00\x42\x08\n\x06result\"%\n\x06Traces\x12\x1b\n\x06traces\x18\x01 \x03(\x0b\x32\x0b.web3.Trace\"\xe3\x01\n\x11TraceWithLocation\x12\x1a\n\x05trace\x18\x01 \x01(\x0b\x32\x0b.web3.Trace\x12!\n\x14transaction_position\x18\x02 \x01(\x04H\x00\x88\x01\x01\x12*\n\x10transaction_hash\x18\x03 \x01(\x0b\x32\x0b.types.H256H\x01\x88\x01\x01\x12\x14\n\x0c\x62lock_number\x18\x04 \x01(\x04\x12\x1f\n\nblock_hash\x18\x05 \x01(\x0b\x32\x0b.types.H256B\x17\n\x15_transaction_positionB\x13\n\x11_transaction_hash\"=\n\x12TracesWithLocation\x12\'\n\x06traces\x18\x01 \x03(\x0b\x32\x17.web3.TraceWithLocation\"V\n\x1aOptionalTracesWithLocation\x12-\n\x06traces\x18\x01 \x01(\x0b\x32\x18.web3.TracesWithLocationH\x00\x88\x01\x01\x42\t\n\x07_traces\"(\n\x0bMemoryDelta\x12\x0b\n\x03off\x18\x01 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"B\n\x0cStorageDelta\x12\x18\n\x03key\x18\x01 \x01(\x0b\x32\x0b.types.H256\x12\x18\n\x03val\x18\x02 \x01(\x0b\x32\x0b.types.H256\"\xab\x01\n\x13VmExecutedOperation\x12\x0c\n\x04used\x18\x01 \x01(\x04\x12\x1e\n\x04push\x18\x02 \x01(\x0b\x32\x0b.types.H256H\x00\x88\x01\x01\x12#\n\x03mem\x18\x03 \x01(\x0b\x32\x11.web3.MemoryDeltaH\x01\x88\x01\x01\x12&\n\x05store\x18\x04 \x01(\x0b\x32\x12.web3.StorageDeltaH\x02\x88\x01\x01\x42\x07\n\x05_pushB\x06\n\x04_memB\x08\n\x06_store\"\x85\x01\n\rVmInstruction\x12\n\n\x02pc\x18\x01 \x01(\r\x12\x0c\n\x04\x63ost\x18\x02 \x01(\x04\x12*\n\x02\x65x\x18\x03 \x01(\x0b\x32\x19.web3.VmExecutedOperationH\x00\x88\x01\x01\x12\x1f\n\x03sub\x18\x04 \x01(\x0b\x32\r.web3.VmTraceH\x01\x88\x01\x01\x42\x05\n\x03_exB\x06\n\x04_sub\"9\n\x07VmTrace\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x0c\x12 \n\x03ops\x18\x02 \x03(\x0b\x32\x13.web3.VmInstruction\"A\n\x0b\x41lteredH256\x12\x19\n\x04\x66rom\x18\x01 \x01(\x0b\x32\x0b.types.H256\x12\x17\n\x02to\x18\x02 \x01(\x0b\x32\x0b.types.H256\"\xa5\x01\n\tDeltaH256\x12+\n\tunchanged\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x1c\n\x05\x61\x64\x64\x65\x64\x18\x02 \x01(\x0b\x32\x0b.types.H256H\x00\x12\x1e\n\x07removed\x18\x03 \x01(\x0b\x32\x0b.types.H256H\x00\x12$\n\x07\x61ltered\x18\x04 \x01(\x0b\x32\x11.web3.AlteredH256H\x00\x42\x07\n\x05\x64\x65lta\"&\n\nAlteredU64\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x04\x12\n\n\x02to\x18\x02 \x01(\x04\"\x89\x01\n\x08\x44\x65ltaU64\x12+\n\tunchanged\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x0f\n\x05\x61\x64\x64\x65\x64\x18\x02 \x01(\x04H\x00\x12\x11\n\x07removed\x18\x03 \x01(\x04H\x00\x12#\n\x07\x61ltered\x18\x04 \x01(\x0b\x32\x10.web3.AlteredU64H\x00\x42\x07\n\x05\x64\x65lta\"(\n\x0c\x41lteredBytes\x12\x0c\n\x04\x66rom\x18\x01 \x01(\x0c\x12\n\n\x02to\x18\x02 \x01(\x0c\"\x8d\x01\n\nDeltaBytes\x12+\n\tunchanged\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00\x12\x0f\n\x05\x61\x64\x64\x65\x64\x18\x02 \x01(\x0cH\x00\x12\x11\n\x07removed\x18\x03 \x01(\x0cH\x00\x12%\n\x07\x61ltered\x18\x04 \x01(\x0b\x32\x12.web3.AlteredBytesH\x00\x42\x07\n\x05\x64\x65lta\"Q\n\x10StorageDiffEntry\x12\x1d\n\x08location\x18\x01 \x01(\x0b\x32\x0b.types.H256\x12\x1e\n\x05\x64\x65lta\x18\x02 \x01(\x0b\x32\x0f.web3.DeltaH256\"\x97\x01\n\x0b\x41\x63\x63ountDiff\x12 \n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x0f.web3.DeltaH256\x12\x1d\n\x05nonce\x18\x02 \x01(\x0b\x32\x0e.web3.DeltaU64\x12\x1e\n\x04\x63ode\x18\x03 \x01(\x0b\x32\x10.web3.DeltaBytes\x12\'\n\x07storage\x18\x04 \x03(\x0b\x32\x16.web3.StorageDiffEntry\"N\n\x10\x41\x63\x63ountDiffEntry\x12\x18\n\x03key\x18\x01 \x01(\x0b\x32\x0b.types.H160\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.web3.AccountDiff\"1\n\tStateDiff\x12$\n\x04\x64iff\x18\x01 \x03(\x0b\x32\x16.web3.AccountDiffEntry\"\xb5\x01\n\tFullTrace\x12\x0e\n\x06output\x18\x01 \x01(\x0c\x12!\n\x06traces\x18\x02 \x01(\x0b\x32\x0c.web3.TracesH\x00\x88\x01\x01\x12$\n\x08vm_trace\x18\x03 \x01(\x0b\x32\r.web3.VmTraceH\x01\x88\x01\x01\x12(\n\nstate_diff\x18\x04 \x01(\x0b\x32\x0f.web3.StateDiffH\x02\x88\x01\x01\x42\t\n\x07_tracesB\x0b\n\t_vm_traceB\r\n\x0b_state_diff\"j\n\x1c\x46ullTraceWithTransactionHash\x12#\n\nfull_trace\x18\x01 \x01(\x0b\x32\x0f.web3.FullTrace\x12%\n\x10transaction_hash\x18\x02 \x01(\x0b\x32\x0b.types.H256\"-\n\nFullTraces\x12\x1f\n\x06traces\x18\x01 \x03(\x0b\x32\x0f.web3.FullTrace\"U\n\x1f\x46ullTracesWithTransactionHashes\x12\x32\n\x06traces\x18\x01 \x03(\x0b\x32\".web3.FullTraceWithTransactionHash\"p\n\'OptionalFullTracesWithTransactionHashes\x12:\n\x06traces\x18\x01 \x01(\x0b\x32%.web3.FullTracesWithTransactionHashesH\x00\x88\x01\x01\x42\t\n\x07_traces*)\n\nFilterMode\x12\t\n\x05Union\x10\x00\x12\x10\n\x0cIntersection\x10\x01*d\n\x08\x43\x61llType\x12\x10\n\x0c\x43\x61llTypeCall\x10\x00\x12\x14\n\x10\x43\x61llTypeCallCode\x10\x01\x12\x18\n\x14\x43\x61llTypeDelegateCall\x10\x02\x12\x16\n\x12\x43\x61llTypeStaticCall\x10\x03\x32\xc8\x02\n\x08TraceApi\x12,\n\x04\x43\x61ll\x12\x12.web3.CallRequests\x1a\x10.web3.FullTraces\x12\x38\n\x05\x42lock\x12\r.web3.BlockId\x1a .web3.OptionalTracesWithLocation\x12[\n\x11\x42lockTransactions\x12\x17.web3.TraceBlockRequest\x1a-.web3.OptionalFullTracesWithTransactionHashes\x12=\n\x0bTransaction\x12\x1d.web3.TraceTransactionRequest\x1a\x0f.web3.FullTrace\x12\x38\n\x06\x46ilter\x12\x13.web3.FilterRequest\x1a\x17.web3.TraceWithLocation0\x01\x62\x06proto3')

_FILTERMODE = DESCRIPTOR.enum_types_by_name['FilterMode']
FilterMode = enum_type_wrapper.EnumTypeWrapper(_FILTERMODE)
_CALLTYPE = DESCRIPTOR.enum_types_by_name['CallType']
CallType = enum_type_wrapper.EnumTypeWrapper(_CALLTYPE)
Union = 0
Intersection = 1
CallTypeCall = 0
CallTypeCallCode = 1
CallTypeDelegateCall = 2
CallTypeStaticCall = 3


_LEGACYCALL = DESCRIPTOR.message_types_by_name['LegacyCall']
_ACCESSLIST = DESCRIPTOR.message_types_by_name['AccessList']
_EIP2930CALL = DESCRIPTOR.message_types_by_name['EIP2930Call']
_EIP1559CALL = DESCRIPTOR.message_types_by_name['EIP1559Call']
_CALL = DESCRIPTOR.message_types_by_name['Call']
_TRACEKINDS = DESCRIPTOR.message_types_by_name['TraceKinds']
_CALLREQUEST = DESCRIPTOR.message_types_by_name['CallRequest']
_CALLREQUESTS = DESCRIPTOR.message_types_by_name['CallRequests']
_TRACEBLOCKREQUEST = DESCRIPTOR.message_types_by_name['TraceBlockRequest']
_TRACETRANSACTIONREQUEST = DESCRIPTOR.message_types_by_name['TraceTransactionRequest']
_ADDRESSSET = DESCRIPTOR.message_types_by_name['AddressSet']
_FILTERREQUEST = DESCRIPTOR.message_types_by_name['FilterRequest']
_CALLACTION = DESCRIPTOR.message_types_by_name['CallAction']
_CREATEACTION = DESCRIPTOR.message_types_by_name['CreateAction']
_SELFDESTRUCTACTION = DESCRIPTOR.message_types_by_name['SelfdestructAction']
_REWARDACTION = DESCRIPTOR.message_types_by_name['RewardAction']
_ACTION = DESCRIPTOR.message_types_by_name['Action']
_TRACE = DESCRIPTOR.message_types_by_name['Trace']
_CALLOUTPUT = DESCRIPTOR.message_types_by_name['CallOutput']
_CREATEOUTPUT = DESCRIPTOR.message_types_by_name['CreateOutput']
_TRACEOUTPUT = DESCRIPTOR.message_types_by_name['TraceOutput']
_TRACERESULT = DESCRIPTOR.message_types_by_name['TraceResult']
_TRACES = DESCRIPTOR.message_types_by_name['Traces']
_TRACEWITHLOCATION = DESCRIPTOR.message_types_by_name['TraceWithLocation']
_TRACESWITHLOCATION = DESCRIPTOR.message_types_by_name['TracesWithLocation']
_OPTIONALTRACESWITHLOCATION = DESCRIPTOR.message_types_by_name['OptionalTracesWithLocation']
_MEMORYDELTA = DESCRIPTOR.message_types_by_name['MemoryDelta']
_STORAGEDELTA = DESCRIPTOR.message_types_by_name['StorageDelta']
_VMEXECUTEDOPERATION = DESCRIPTOR.message_types_by_name['VmExecutedOperation']
_VMINSTRUCTION = DESCRIPTOR.message_types_by_name['VmInstruction']
_VMTRACE = DESCRIPTOR.message_types_by_name['VmTrace']
_ALTEREDH256 = DESCRIPTOR.message_types_by_name['AlteredH256']
_DELTAH256 = DESCRIPTOR.message_types_by_name['DeltaH256']
_ALTEREDU64 = DESCRIPTOR.message_types_by_name['AlteredU64']
_DELTAU64 = DESCRIPTOR.message_types_by_name['DeltaU64']
_ALTEREDBYTES = DESCRIPTOR.message_types_by_name['AlteredBytes']
_DELTABYTES = DESCRIPTOR.message_types_by_name['DeltaBytes']
_STORAGEDIFFENTRY = DESCRIPTOR.message_types_by_name['StorageDiffEntry']
_ACCOUNTDIFF = DESCRIPTOR.message_types_by_name['AccountDiff']
_ACCOUNTDIFFENTRY = DESCRIPTOR.message_types_by_name['AccountDiffEntry']
_STATEDIFF = DESCRIPTOR.message_types_by_name['StateDiff']
_FULLTRACE = DESCRIPTOR.message_types_by_name['FullTrace']
_FULLTRACEWITHTRANSACTIONHASH = DESCRIPTOR.message_types_by_name['FullTraceWithTransactionHash']
_FULLTRACES = DESCRIPTOR.message_types_by_name['FullTraces']
_FULLTRACESWITHTRANSACTIONHASHES = DESCRIPTOR.message_types_by_name['FullTracesWithTransactionHashes']
_OPTIONALFULLTRACESWITHTRANSACTIONHASHES = DESCRIPTOR.message_types_by_name['OptionalFullTracesWithTransactionHashes']
_REWARDACTION_REWARDTYPE = _REWARDACTION.enum_types_by_name['RewardType']
LegacyCall = _reflection.GeneratedProtocolMessageType('LegacyCall', (_message.Message,), {
  'DESCRIPTOR' : _LEGACYCALL,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.LegacyCall)
  })
_sym_db.RegisterMessage(LegacyCall)

AccessList = _reflection.GeneratedProtocolMessageType('AccessList', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSLIST,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.AccessList)
  })
_sym_db.RegisterMessage(AccessList)

EIP2930Call = _reflection.GeneratedProtocolMessageType('EIP2930Call', (_message.Message,), {
  'DESCRIPTOR' : _EIP2930CALL,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.EIP2930Call)
  })
_sym_db.RegisterMessage(EIP2930Call)

EIP1559Call = _reflection.GeneratedProtocolMessageType('EIP1559Call', (_message.Message,), {
  'DESCRIPTOR' : _EIP1559CALL,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.EIP1559Call)
  })
_sym_db.RegisterMessage(EIP1559Call)

Call = _reflection.GeneratedProtocolMessageType('Call', (_message.Message,), {
  'DESCRIPTOR' : _CALL,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.Call)
  })
_sym_db.RegisterMessage(Call)

TraceKinds = _reflection.GeneratedProtocolMessageType('TraceKinds', (_message.Message,), {
  'DESCRIPTOR' : _TRACEKINDS,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.TraceKinds)
  })
_sym_db.RegisterMessage(TraceKinds)

CallRequest = _reflection.GeneratedProtocolMessageType('CallRequest', (_message.Message,), {
  'DESCRIPTOR' : _CALLREQUEST,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.CallRequest)
  })
_sym_db.RegisterMessage(CallRequest)

CallRequests = _reflection.GeneratedProtocolMessageType('CallRequests', (_message.Message,), {
  'DESCRIPTOR' : _CALLREQUESTS,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.CallRequests)
  })
_sym_db.RegisterMessage(CallRequests)

TraceBlockRequest = _reflection.GeneratedProtocolMessageType('TraceBlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRACEBLOCKREQUEST,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.TraceBlockRequest)
  })
_sym_db.RegisterMessage(TraceBlockRequest)

TraceTransactionRequest = _reflection.GeneratedProtocolMessageType('TraceTransactionRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRACETRANSACTIONREQUEST,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.TraceTransactionRequest)
  })
_sym_db.RegisterMessage(TraceTransactionRequest)

AddressSet = _reflection.GeneratedProtocolMessageType('AddressSet', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSSET,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.AddressSet)
  })
_sym_db.RegisterMessage(AddressSet)

FilterRequest = _reflection.GeneratedProtocolMessageType('FilterRequest', (_message.Message,), {
  'DESCRIPTOR' : _FILTERREQUEST,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.FilterRequest)
  })
_sym_db.RegisterMessage(FilterRequest)

CallAction = _reflection.GeneratedProtocolMessageType('CallAction', (_message.Message,), {
  'DESCRIPTOR' : _CALLACTION,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.CallAction)
  })
_sym_db.RegisterMessage(CallAction)

CreateAction = _reflection.GeneratedProtocolMessageType('CreateAction', (_message.Message,), {
  'DESCRIPTOR' : _CREATEACTION,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.CreateAction)
  })
_sym_db.RegisterMessage(CreateAction)

SelfdestructAction = _reflection.GeneratedProtocolMessageType('SelfdestructAction', (_message.Message,), {
  'DESCRIPTOR' : _SELFDESTRUCTACTION,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.SelfdestructAction)
  })
_sym_db.RegisterMessage(SelfdestructAction)

RewardAction = _reflection.GeneratedProtocolMessageType('RewardAction', (_message.Message,), {
  'DESCRIPTOR' : _REWARDACTION,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.RewardAction)
  })
_sym_db.RegisterMessage(RewardAction)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), {
  'DESCRIPTOR' : _ACTION,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.Action)
  })
_sym_db.RegisterMessage(Action)

Trace = _reflection.GeneratedProtocolMessageType('Trace', (_message.Message,), {
  'DESCRIPTOR' : _TRACE,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.Trace)
  })
_sym_db.RegisterMessage(Trace)

CallOutput = _reflection.GeneratedProtocolMessageType('CallOutput', (_message.Message,), {
  'DESCRIPTOR' : _CALLOUTPUT,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.CallOutput)
  })
_sym_db.RegisterMessage(CallOutput)

CreateOutput = _reflection.GeneratedProtocolMessageType('CreateOutput', (_message.Message,), {
  'DESCRIPTOR' : _CREATEOUTPUT,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.CreateOutput)
  })
_sym_db.RegisterMessage(CreateOutput)

TraceOutput = _reflection.GeneratedProtocolMessageType('TraceOutput', (_message.Message,), {
  'DESCRIPTOR' : _TRACEOUTPUT,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.TraceOutput)
  })
_sym_db.RegisterMessage(TraceOutput)

TraceResult = _reflection.GeneratedProtocolMessageType('TraceResult', (_message.Message,), {
  'DESCRIPTOR' : _TRACERESULT,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.TraceResult)
  })
_sym_db.RegisterMessage(TraceResult)

Traces = _reflection.GeneratedProtocolMessageType('Traces', (_message.Message,), {
  'DESCRIPTOR' : _TRACES,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.Traces)
  })
_sym_db.RegisterMessage(Traces)

TraceWithLocation = _reflection.GeneratedProtocolMessageType('TraceWithLocation', (_message.Message,), {
  'DESCRIPTOR' : _TRACEWITHLOCATION,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.TraceWithLocation)
  })
_sym_db.RegisterMessage(TraceWithLocation)

TracesWithLocation = _reflection.GeneratedProtocolMessageType('TracesWithLocation', (_message.Message,), {
  'DESCRIPTOR' : _TRACESWITHLOCATION,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.TracesWithLocation)
  })
_sym_db.RegisterMessage(TracesWithLocation)

OptionalTracesWithLocation = _reflection.GeneratedProtocolMessageType('OptionalTracesWithLocation', (_message.Message,), {
  'DESCRIPTOR' : _OPTIONALTRACESWITHLOCATION,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.OptionalTracesWithLocation)
  })
_sym_db.RegisterMessage(OptionalTracesWithLocation)

MemoryDelta = _reflection.GeneratedProtocolMessageType('MemoryDelta', (_message.Message,), {
  'DESCRIPTOR' : _MEMORYDELTA,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.MemoryDelta)
  })
_sym_db.RegisterMessage(MemoryDelta)

StorageDelta = _reflection.GeneratedProtocolMessageType('StorageDelta', (_message.Message,), {
  'DESCRIPTOR' : _STORAGEDELTA,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.StorageDelta)
  })
_sym_db.RegisterMessage(StorageDelta)

VmExecutedOperation = _reflection.GeneratedProtocolMessageType('VmExecutedOperation', (_message.Message,), {
  'DESCRIPTOR' : _VMEXECUTEDOPERATION,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.VmExecutedOperation)
  })
_sym_db.RegisterMessage(VmExecutedOperation)

VmInstruction = _reflection.GeneratedProtocolMessageType('VmInstruction', (_message.Message,), {
  'DESCRIPTOR' : _VMINSTRUCTION,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.VmInstruction)
  })
_sym_db.RegisterMessage(VmInstruction)

VmTrace = _reflection.GeneratedProtocolMessageType('VmTrace', (_message.Message,), {
  'DESCRIPTOR' : _VMTRACE,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.VmTrace)
  })
_sym_db.RegisterMessage(VmTrace)

AlteredH256 = _reflection.GeneratedProtocolMessageType('AlteredH256', (_message.Message,), {
  'DESCRIPTOR' : _ALTEREDH256,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.AlteredH256)
  })
_sym_db.RegisterMessage(AlteredH256)

DeltaH256 = _reflection.GeneratedProtocolMessageType('DeltaH256', (_message.Message,), {
  'DESCRIPTOR' : _DELTAH256,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.DeltaH256)
  })
_sym_db.RegisterMessage(DeltaH256)

AlteredU64 = _reflection.GeneratedProtocolMessageType('AlteredU64', (_message.Message,), {
  'DESCRIPTOR' : _ALTEREDU64,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.AlteredU64)
  })
_sym_db.RegisterMessage(AlteredU64)

DeltaU64 = _reflection.GeneratedProtocolMessageType('DeltaU64', (_message.Message,), {
  'DESCRIPTOR' : _DELTAU64,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.DeltaU64)
  })
_sym_db.RegisterMessage(DeltaU64)

AlteredBytes = _reflection.GeneratedProtocolMessageType('AlteredBytes', (_message.Message,), {
  'DESCRIPTOR' : _ALTEREDBYTES,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.AlteredBytes)
  })
_sym_db.RegisterMessage(AlteredBytes)

DeltaBytes = _reflection.GeneratedProtocolMessageType('DeltaBytes', (_message.Message,), {
  'DESCRIPTOR' : _DELTABYTES,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.DeltaBytes)
  })
_sym_db.RegisterMessage(DeltaBytes)

StorageDiffEntry = _reflection.GeneratedProtocolMessageType('StorageDiffEntry', (_message.Message,), {
  'DESCRIPTOR' : _STORAGEDIFFENTRY,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.StorageDiffEntry)
  })
_sym_db.RegisterMessage(StorageDiffEntry)

AccountDiff = _reflection.GeneratedProtocolMessageType('AccountDiff', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTDIFF,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.AccountDiff)
  })
_sym_db.RegisterMessage(AccountDiff)

AccountDiffEntry = _reflection.GeneratedProtocolMessageType('AccountDiffEntry', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTDIFFENTRY,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.AccountDiffEntry)
  })
_sym_db.RegisterMessage(AccountDiffEntry)

StateDiff = _reflection.GeneratedProtocolMessageType('StateDiff', (_message.Message,), {
  'DESCRIPTOR' : _STATEDIFF,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.StateDiff)
  })
_sym_db.RegisterMessage(StateDiff)

FullTrace = _reflection.GeneratedProtocolMessageType('FullTrace', (_message.Message,), {
  'DESCRIPTOR' : _FULLTRACE,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.FullTrace)
  })
_sym_db.RegisterMessage(FullTrace)

FullTraceWithTransactionHash = _reflection.GeneratedProtocolMessageType('FullTraceWithTransactionHash', (_message.Message,), {
  'DESCRIPTOR' : _FULLTRACEWITHTRANSACTIONHASH,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.FullTraceWithTransactionHash)
  })
_sym_db.RegisterMessage(FullTraceWithTransactionHash)

FullTraces = _reflection.GeneratedProtocolMessageType('FullTraces', (_message.Message,), {
  'DESCRIPTOR' : _FULLTRACES,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.FullTraces)
  })
_sym_db.RegisterMessage(FullTraces)

FullTracesWithTransactionHashes = _reflection.GeneratedProtocolMessageType('FullTracesWithTransactionHashes', (_message.Message,), {
  'DESCRIPTOR' : _FULLTRACESWITHTRANSACTIONHASHES,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.FullTracesWithTransactionHashes)
  })
_sym_db.RegisterMessage(FullTracesWithTransactionHashes)

OptionalFullTracesWithTransactionHashes = _reflection.GeneratedProtocolMessageType('OptionalFullTracesWithTransactionHashes', (_message.Message,), {
  'DESCRIPTOR' : _OPTIONALFULLTRACESWITHTRANSACTIONHASHES,
  '__module__' : 'web3.trace_pb2'
  # @@protoc_insertion_point(class_scope:web3.OptionalFullTracesWithTransactionHashes)
  })
_sym_db.RegisterMessage(OptionalFullTracesWithTransactionHashes)

_TRACEAPI = DESCRIPTOR.services_by_name['TraceApi']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILTERMODE._serialized_start=5522
  _FILTERMODE._serialized_end=5563
  _CALLTYPE._serialized_start=5565
  _CALLTYPE._serialized_end=5665
  _LEGACYCALL._serialized_start=94
  _LEGACYCALL._serialized_end=333
  _ACCESSLIST._serialized_start=335
  _ACCESSLIST._serialized_end=390
  _EIP2930CALL._serialized_start=393
  _EIP2930CALL._serialized_end=693
  _EIP1559CALL._serialized_start=696
  _EIP1559CALL._serialized_end=1076
  _CALL._serialized_start=1078
  _CALL._serialized_end=1204
  _TRACEKINDS._serialized_start=1206
  _TRACEKINDS._serialized_end=1271
  _CALLREQUEST._serialized_start=1273
  _CALLREQUEST._serialized_end=1345
  _CALLREQUESTS._serialized_start=1347
  _CALLREQUESTS._serialized_end=1428
  _TRACEBLOCKREQUEST._serialized_start=1430
  _TRACEBLOCKREQUEST._serialized_end=1509
  _TRACETRANSACTIONREQUEST._serialized_start=1511
  _TRACETRANSACTIONREQUEST._serialized_end=1596
  _ADDRESSSET._serialized_start=1598
  _ADDRESSSET._serialized_end=1642
  _FILTERREQUEST._serialized_start=1645
  _FILTERREQUEST._serialized_end=1940
  _CALLACTION._serialized_start=1943
  _CALLACTION._serialized_end=2117
  _CREATEACTION._serialized_start=2119
  _CREATEACTION._serialized_end=2215
  _SELFDESTRUCTACTION._serialized_start=2217
  _SELFDESTRUCTACTION._serialized_end=2334
  _REWARDACTION._serialized_start=2337
  _REWARDACTION._serialized_end=2496
  _REWARDACTION_REWARDTYPE._serialized_start=2462
  _REWARDACTION_REWARDTYPE._serialized_end=2496
  _ACTION._serialized_start=2499
  _ACTION._serialized_end=2677
  _TRACE._serialized_start=2680
  _TRACE._serialized_end=2810
  _CALLOUTPUT._serialized_start=2812
  _CALLOUTPUT._serialized_end=2858
  _CREATEOUTPUT._serialized_start=2860
  _CREATEOUTPUT._serialized_end=2936
  _TRACEOUTPUT._serialized_start=2938
  _TRACEOUTPUT._serialized_end=3033
  _TRACERESULT._serialized_start=3035
  _TRACERESULT._serialized_end=3112
  _TRACES._serialized_start=3114
  _TRACES._serialized_end=3151
  _TRACEWITHLOCATION._serialized_start=3154
  _TRACEWITHLOCATION._serialized_end=3381
  _TRACESWITHLOCATION._serialized_start=3383
  _TRACESWITHLOCATION._serialized_end=3444
  _OPTIONALTRACESWITHLOCATION._serialized_start=3446
  _OPTIONALTRACESWITHLOCATION._serialized_end=3532
  _MEMORYDELTA._serialized_start=3534
  _MEMORYDELTA._serialized_end=3574
  _STORAGEDELTA._serialized_start=3576
  _STORAGEDELTA._serialized_end=3642
  _VMEXECUTEDOPERATION._serialized_start=3645
  _VMEXECUTEDOPERATION._serialized_end=3816
  _VMINSTRUCTION._serialized_start=3819
  _VMINSTRUCTION._serialized_end=3952
  _VMTRACE._serialized_start=3954
  _VMTRACE._serialized_end=4011
  _ALTEREDH256._serialized_start=4013
  _ALTEREDH256._serialized_end=4078
  _DELTAH256._serialized_start=4081
  _DELTAH256._serialized_end=4246
  _ALTEREDU64._serialized_start=4248
  _ALTEREDU64._serialized_end=4286
  _DELTAU64._serialized_start=4289
  _DELTAU64._serialized_end=4426
  _ALTEREDBYTES._serialized_start=4428
  _ALTEREDBYTES._serialized_end=4468
  _DELTABYTES._serialized_start=4471
  _DELTABYTES._serialized_end=4612
  _STORAGEDIFFENTRY._serialized_start=4614
  _STORAGEDIFFENTRY._serialized_end=4695
  _ACCOUNTDIFF._serialized_start=4698
  _ACCOUNTDIFF._serialized_end=4849
  _ACCOUNTDIFFENTRY._serialized_start=4851
  _ACCOUNTDIFFENTRY._serialized_end=4929
  _STATEDIFF._serialized_start=4931
  _STATEDIFF._serialized_end=4980
  _FULLTRACE._serialized_start=4983
  _FULLTRACE._serialized_end=5164
  _FULLTRACEWITHTRANSACTIONHASH._serialized_start=5166
  _FULLTRACEWITHTRANSACTIONHASH._serialized_end=5272
  _FULLTRACES._serialized_start=5274
  _FULLTRACES._serialized_end=5319
  _FULLTRACESWITHTRANSACTIONHASHES._serialized_start=5321
  _FULLTRACESWITHTRANSACTIONHASHES._serialized_end=5406
  _OPTIONALFULLTRACESWITHTRANSACTIONHASHES._serialized_start=5408
  _OPTIONALFULLTRACESWITHTRANSACTIONHASHES._serialized_end=5520
  _TRACEAPI._serialized_start=5668
  _TRACEAPI._serialized_end=5996
# @@protoc_insertion_point(module_scope)