# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from interbotix_sdk/OperatingModesRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class OperatingModesRequest(genpy.Message):
  _md5sum = "585951edcc6006e2034f68a456aad669"
  _type = "interbotix_sdk/OperatingModesRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Set the operating modes for the arm, gripper, or a single joint
#
# There are four options when setting operating modes:
#   1) ARM_JOINTS_AND_GRIPPER - affects the operating modes for all joints, including the gripper.
#   2) ARM_JOINTS - affects the operating modes for all joints, excluding the gripper.
#   3) GRIPPER - affects the operating mode only for the gripper
#   4) SINGLE_JOINT - affects the operating mode for the joint specified by 'joint_name'.
#                     Note that the 'joint_name' parameter only needs to be used for this
#                     option. For any other option, it can be left blank.
# Set the option to the 'cmd' parameter and the 'joint_name' to the specified joint (if doing the
# SINGLE_JOINT option).

# There are 5 valid operating modes for the arm. They are...
#   "none" - arm motors will not respond to any joint command
#   "position" - arm motors will expect only position commands
#   "velocity" - arm motors will expect only velocity commands
#   "current" - arm motors will expect only current commands
#   "pwm" - arm motors will expect only pwm commands
#
# The gripper can also be set to "ext_position". This allows the gripper to do
# multiple rotations instead of just one. It should only be used if you are using
# a custom gripper capable of doing more than one rotation.
#
# For "position" control, profile_velocity sets the max speed of each joint while
# profile_acceleration sets the max acceleration. Please reference the motor datasheet
# (just click a motor at http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_workbench/)
# for conversion factors. Values can be between 0 and 32,767. If setting custom profiles,
# make sure to set 'use_custom_x_profiles' to true.
#
# For "velocity" control, only profile_acceleration is used.
#
# The velocity and acceleration profiles are not used in the "current" and "pwm" modes.

int8 ARM_JOINTS_AND_GRIPPER = 1
int8 ARM_JOINTS = 2
int8 GRIPPER = 3
int8 SINGLE_JOINT = 4

int8 cmd
string mode
string joint_name
bool use_custom_profiles
int32 profile_velocity
int32 profile_acceleration
"""
  # Pseudo-constants
  ARM_JOINTS_AND_GRIPPER = 1
  ARM_JOINTS = 2
  GRIPPER = 3
  SINGLE_JOINT = 4

  __slots__ = ['cmd','mode','joint_name','use_custom_profiles','profile_velocity','profile_acceleration']
  _slot_types = ['int8','string','string','bool','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       cmd,mode,joint_name,use_custom_profiles,profile_velocity,profile_acceleration

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(OperatingModesRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.cmd is None:
        self.cmd = 0
      if self.mode is None:
        self.mode = ''
      if self.joint_name is None:
        self.joint_name = ''
      if self.use_custom_profiles is None:
        self.use_custom_profiles = False
      if self.profile_velocity is None:
        self.profile_velocity = 0
      if self.profile_acceleration is None:
        self.profile_acceleration = 0
    else:
      self.cmd = 0
      self.mode = ''
      self.joint_name = ''
      self.use_custom_profiles = False
      self.profile_velocity = 0
      self.profile_acceleration = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.cmd
      buff.write(_get_struct_b().pack(_x))
      _x = self.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.joint_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B2i().pack(_x.use_custom_profiles, _x.profile_velocity, _x.profile_acceleration))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.cmd,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.joint_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.joint_name = str[start:end]
      _x = self
      start = end
      end += 9
      (_x.use_custom_profiles, _x.profile_velocity, _x.profile_acceleration,) = _get_struct_B2i().unpack(str[start:end])
      self.use_custom_profiles = bool(self.use_custom_profiles)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.cmd
      buff.write(_get_struct_b().pack(_x))
      _x = self.mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.joint_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B2i().pack(_x.use_custom_profiles, _x.profile_velocity, _x.profile_acceleration))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 1
      (self.cmd,) = _get_struct_b().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.mode = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.joint_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.joint_name = str[start:end]
      _x = self
      start = end
      end += 9
      (_x.use_custom_profiles, _x.profile_velocity, _x.profile_acceleration,) = _get_struct_B2i().unpack(str[start:end])
      self.use_custom_profiles = bool(self.use_custom_profiles)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B2i = None
def _get_struct_B2i():
    global _struct_B2i
    if _struct_B2i is None:
        _struct_B2i = struct.Struct("<B2i")
    return _struct_B2i
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from interbotix_sdk/OperatingModesResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class OperatingModesResponse(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "interbotix_sdk/OperatingModesResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(OperatingModesResponse, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
class OperatingModes(object):
  _type          = 'interbotix_sdk/OperatingModes'
  _md5sum = '585951edcc6006e2034f68a456aad669'
  _request_class  = OperatingModesRequest
  _response_class = OperatingModesResponse
