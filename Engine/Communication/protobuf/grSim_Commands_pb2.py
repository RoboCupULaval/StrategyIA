# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grSim_Commands.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grSim_Commands.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x14grSim_Commands.proto\"\xea\x01\n\x13grSim_Robot_Command\x12\n\n\x02id\x18\x01 \x02(\r\x12\x12\n\nkickspeedx\x18\x02 \x02(\x02\x12\x12\n\nkickspeedz\x18\x03 \x02(\x02\x12\x12\n\nveltangent\x18\x04 \x02(\x02\x12\x11\n\tvelnormal\x18\x05 \x02(\x02\x12\x12\n\nvelangular\x18\x06 \x02(\x02\x12\x0f\n\x07spinner\x18\x07 \x02(\x08\x12\x13\n\x0bwheelsspeed\x18\x08 \x02(\x08\x12\x0e\n\x06wheel1\x18\t \x01(\x02\x12\x0e\n\x06wheel2\x18\n \x01(\x02\x12\x0e\n\x06wheel3\x18\x0b \x01(\x02\x12\x0e\n\x06wheel4\x18\x0c \x01(\x02\"g\n\x0egrSim_Commands\x12\x11\n\ttimestamp\x18\x01 \x02(\x01\x12\x14\n\x0cisteamyellow\x18\x02 \x02(\x08\x12,\n\x0erobot_commands\x18\x03 \x03(\x0b\x32\x14.grSim_Robot_Command')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GRSIM_ROBOT_COMMAND = _descriptor.Descriptor(
  name='grSim_Robot_Command',
  full_name='grSim_Robot_Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grSim_Robot_Command.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kickspeedx', full_name='grSim_Robot_Command.kickspeedx', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='kickspeedz', full_name='grSim_Robot_Command.kickspeedz', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='veltangent', full_name='grSim_Robot_Command.veltangent', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velnormal', full_name='grSim_Robot_Command.velnormal', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='velangular', full_name='grSim_Robot_Command.velangular', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spinner', full_name='grSim_Robot_Command.spinner', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wheelsspeed', full_name='grSim_Robot_Command.wheelsspeed', index=7,
      number=8, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wheel1', full_name='grSim_Robot_Command.wheel1', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wheel2', full_name='grSim_Robot_Command.wheel2', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wheel3', full_name='grSim_Robot_Command.wheel3', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wheel4', full_name='grSim_Robot_Command.wheel4', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=259,
)


_GRSIM_COMMANDS = _descriptor.Descriptor(
  name='grSim_Commands',
  full_name='grSim_Commands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='grSim_Commands.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isteamyellow', full_name='grSim_Commands.isteamyellow', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='robot_commands', full_name='grSim_Commands.robot_commands', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=364,
)

_GRSIM_COMMANDS.fields_by_name['robot_commands'].message_type = _GRSIM_ROBOT_COMMAND
DESCRIPTOR.message_types_by_name['grSim_Robot_Command'] = _GRSIM_ROBOT_COMMAND
DESCRIPTOR.message_types_by_name['grSim_Commands'] = _GRSIM_COMMANDS

grSim_Robot_Command = _reflection.GeneratedProtocolMessageType('grSim_Robot_Command', (_message.Message,), dict(
  DESCRIPTOR = _GRSIM_ROBOT_COMMAND,
  __module__ = 'grSim_Commands_pb2'
  # @@protoc_insertion_point(class_scope:grSim_Robot_Command)
  ))
_sym_db.RegisterMessage(grSim_Robot_Command)

grSim_Commands = _reflection.GeneratedProtocolMessageType('grSim_Commands', (_message.Message,), dict(
  DESCRIPTOR = _GRSIM_COMMANDS,
  __module__ = 'grSim_Commands_pb2'
  # @@protoc_insertion_point(class_scope:grSim_Commands)
  ))
_sym_db.RegisterMessage(grSim_Commands)


# @@protoc_insertion_point(module_scope)
