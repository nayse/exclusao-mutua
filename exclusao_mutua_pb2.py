# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exclusao_mutua.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x65xclusao_mutua.proto\x12\x0e\x65xclusao_mutua\"(\n\x12RequisicaoRegistro\x12\x12\n\ncliente_id\x18\x01 \x01(\x05\"\x12\n\x10RespostaRegistro\"&\n\x10RequisicaoAcesso\x12\x12\n\ncliente_id\x18\x01 \x01(\x05\"#\n\x0eRespostaAcesso\x12\x11\n\tpermitido\x18\x01 \x01(\x08\")\n\x13RequisicaoLiberacao\x12\x12\n\ncliente_id\x18\x01 \x01(\x05\"\x13\n\x11RespostaLiberacao2\x9d\x02\n\rExclusaoMutua\x12Z\n\x10RegistrarCliente\x12\".exclusao_mutua.RequisicaoRegistro\x1a .exclusao_mutua.RespostaRegistro\"\x00\x12U\n\x0fSolicitarAcesso\x12 .exclusao_mutua.RequisicaoAcesso\x1a\x1e.exclusao_mutua.RespostaAcesso\"\x00\x12Y\n\rLiberarAcesso\x12#.exclusao_mutua.RequisicaoLiberacao\x1a!.exclusao_mutua.RespostaLiberacao\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exclusao_mutua_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUISICAOREGISTRO._serialized_start=40
  _REQUISICAOREGISTRO._serialized_end=80
  _RESPOSTAREGISTRO._serialized_start=82
  _RESPOSTAREGISTRO._serialized_end=100
  _REQUISICAOACESSO._serialized_start=102
  _REQUISICAOACESSO._serialized_end=140
  _RESPOSTAACESSO._serialized_start=142
  _RESPOSTAACESSO._serialized_end=177
  _REQUISICAOLIBERACAO._serialized_start=179
  _REQUISICAOLIBERACAO._serialized_end=220
  _RESPOSTALIBERACAO._serialized_start=222
  _RESPOSTALIBERACAO._serialized_end=241
  _EXCLUSAOMUTUA._serialized_start=244
  _EXCLUSAOMUTUA._serialized_end=529
# @@protoc_insertion_point(module_scope)
