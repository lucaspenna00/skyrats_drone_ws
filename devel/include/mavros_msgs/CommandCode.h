// Generated by gencpp from file mavros_msgs/CommandCode.msg
// DO NOT EDIT!


#ifndef MAVROS_MSGS_MESSAGE_COMMANDCODE_H
#define MAVROS_MSGS_MESSAGE_COMMANDCODE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mavros_msgs
{
template <class ContainerAllocator>
struct CommandCode_
{
  typedef CommandCode_<ContainerAllocator> Type;

  CommandCode_()
    {
    }
  CommandCode_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }





  enum {
    CMD_DO_SET_MODE = 176u,
    CMD_DO_JUMP = 177u,
    CMD_DO_CHANGE_SPEED = 178u,
    CMD_DO_SET_HOME = 179u,
    CMD_DO_SET_RELAY = 181u,
    CMD_DO_REPEAT_RELAY = 182u,
    CMD_DO_SET_SERVO = 183u,
    CMD_DO_REPEAT_SERVO = 184u,
    CMD_DO_CONTROL_VIDEO = 200u,
    CMD_DO_SET_ROI = 201u,
    CMD_DO_MOUNT_CONTROL = 205u,
    CMD_DO_SET_CAM_TRIGG_DIST = 206u,
    CMD_DO_FENCE_ENABLE = 207u,
    CMD_DO_PARACHUTE = 208u,
    CMD_DO_INVERTED_FLIGHT = 210u,
    CMD_DO_MOUNT_CONTROL_QUAT = 220u,
    CMD_PREFLIGHT_CALIBRATION = 241u,
    CMD_MISSION_START = 300u,
    CMD_COMPONENT_ARM_DISARM = 400u,
    CMD_GET_HOME_POSITION = 410u,
    CMD_START_RX_PAIR = 500u,
    CMD_REQUEST_AUTOPILOT_CAPABILITIES = 520u,
    CMD_DO_TRIGGER_CONTROL = 2003u,
    NAV_WAYPOINT = 16u,
    NAV_LOITER_UNLIM = 17u,
    NAV_LOITER_TURNS = 18u,
    NAV_LOITER_TIME = 19u,
    NAV_RETURN_TO_LAUNCH = 20u,
    NAV_LAND = 21u,
    NAV_TAKEOFF = 22u,
  };


  typedef boost::shared_ptr< ::mavros_msgs::CommandCode_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mavros_msgs::CommandCode_<ContainerAllocator> const> ConstPtr;

}; // struct CommandCode_

typedef ::mavros_msgs::CommandCode_<std::allocator<void> > CommandCode;

typedef boost::shared_ptr< ::mavros_msgs::CommandCode > CommandCodePtr;
typedef boost::shared_ptr< ::mavros_msgs::CommandCode const> CommandCodeConstPtr;

// constants requiring out of line definition

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mavros_msgs::CommandCode_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mavros_msgs::CommandCode_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mavros_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geographic_msgs': ['/opt/ros/lunar/share/geographic_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/lunar/share/sensor_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/lunar/share/std_msgs/cmake/../msg'], 'mavros_msgs': ['/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg'], 'geometry_msgs': ['/opt/ros/lunar/share/geometry_msgs/cmake/../msg'], 'uuid_msgs': ['/opt/ros/lunar/share/uuid_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mavros_msgs::CommandCode_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mavros_msgs::CommandCode_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mavros_msgs::CommandCode_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mavros_msgs::CommandCode_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mavros_msgs::CommandCode_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mavros_msgs::CommandCode_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mavros_msgs::CommandCode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5f2b024f460e58b487bc6e944e943789";
  }

  static const char* value(const ::mavros_msgs::CommandCode_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5f2b024f460e58b4ULL;
  static const uint64_t static_value2 = 0x87bc6e944e943789ULL;
};

template<class ContainerAllocator>
struct DataType< ::mavros_msgs::CommandCode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mavros_msgs/CommandCode";
  }

  static const char* value(const ::mavros_msgs::CommandCode_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mavros_msgs::CommandCode_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Some MAV_CMD command codes.\n\
# Actual meaning and params you may find in MAVLink documentation\n\
# http://mavlink.org/messages/common#ENUM_MAV_CMD\n\
\n\
# some common MAV_CMD\n\
uint16 CMD_DO_SET_MODE = 176\n\
uint16 CMD_DO_JUMP = 177\n\
uint16 CMD_DO_CHANGE_SPEED = 178\n\
uint16 CMD_DO_SET_HOME = 179\n\
uint16 CMD_DO_SET_RELAY = 181\n\
uint16 CMD_DO_REPEAT_RELAY = 182\n\
uint16 CMD_DO_SET_SERVO = 183\n\
uint16 CMD_DO_REPEAT_SERVO = 184\n\
uint16 CMD_DO_CONTROL_VIDEO = 200\n\
uint16 CMD_DO_SET_ROI = 201\n\
uint16 CMD_DO_MOUNT_CONTROL = 205\n\
uint16 CMD_DO_SET_CAM_TRIGG_DIST = 206\n\
uint16 CMD_DO_FENCE_ENABLE = 207\n\
uint16 CMD_DO_PARACHUTE = 208\n\
uint16 CMD_DO_INVERTED_FLIGHT = 210\n\
uint16 CMD_DO_MOUNT_CONTROL_QUAT = 220\n\
uint16 CMD_PREFLIGHT_CALIBRATION = 241\n\
uint16 CMD_MISSION_START = 300\n\
uint16 CMD_COMPONENT_ARM_DISARM = 400\n\
uint16 CMD_GET_HOME_POSITION = 410\n\
uint16 CMD_START_RX_PAIR = 500\n\
uint16 CMD_REQUEST_AUTOPILOT_CAPABILITIES = 520\n\
uint16 CMD_DO_TRIGGER_CONTROL = 2003\n\
\n\
# Waypoint related commands\n\
uint16 NAV_WAYPOINT = 16\n\
uint16 NAV_LOITER_UNLIM = 17\n\
uint16 NAV_LOITER_TURNS = 18\n\
uint16 NAV_LOITER_TIME = 19\n\
uint16 NAV_RETURN_TO_LAUNCH = 20\n\
uint16 NAV_LAND = 21\n\
uint16 NAV_TAKEOFF = 22\n\
";
  }

  static const char* value(const ::mavros_msgs::CommandCode_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mavros_msgs::CommandCode_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CommandCode_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mavros_msgs::CommandCode_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::mavros_msgs::CommandCode_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // MAVROS_MSGS_MESSAGE_COMMANDCODE_H
