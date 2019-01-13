# Install script for directory: /home/lucas/catkin_ws/src/mavros/mavros_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/lucas/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mavros_msgs/msg" TYPE FILE FILES
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/ADSBVehicle.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/ActuatorControl.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/Altitude.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/AttitudeTarget.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/BatteryStatus.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/CamIMUStamp.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/CommandCode.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/DebugValue.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/ExtendedState.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/FileEntry.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/GlobalPositionTarget.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/HilActuatorControls.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/HilControls.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/HilGPS.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/HilSensor.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/HilStateQuaternion.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/HomePosition.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/ManualControl.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/Mavlink.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/OpticalFlowRad.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/OverrideRCIn.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/ParamValue.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/PositionTarget.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/RCIn.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/RCOut.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/RadioStatus.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/State.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/Thrust.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/VFR_HUD.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/Vibration.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/Waypoint.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/WaypointList.msg"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/msg/WaypointReached.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mavros_msgs/srv" TYPE FILE FILES
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/CommandBool.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/CommandHome.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/CommandInt.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/CommandLong.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/CommandTOL.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/CommandTriggerControl.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileChecksum.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileClose.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileList.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileMakeDir.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileOpen.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileRead.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileRemove.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileRemoveDir.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileRename.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileTruncate.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/FileWrite.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/ParamGet.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/ParamPull.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/ParamPush.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/ParamSet.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/SetMavFrame.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/SetMode.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/StreamRate.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/WaypointClear.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/WaypointPull.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/WaypointPush.srv"
    "/home/lucas/catkin_ws/src/mavros/mavros_msgs/srv/WaypointSetCurrent.srv"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mavros_msgs/cmake" TYPE FILE FILES "/home/lucas/catkin_ws/build/mavros/mavros_msgs/catkin_generated/installspace/mavros_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/lucas/catkin_ws/devel/include/mavros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/lucas/catkin_ws/devel/share/roseus/ros/mavros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/lucas/catkin_ws/devel/share/common-lisp/ros/mavros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/lucas/catkin_ws/devel/share/gennodejs/ros/mavros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/lucas/catkin_ws/devel/lib/python2.7/dist-packages/mavros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/lucas/catkin_ws/devel/lib/python2.7/dist-packages/mavros_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/lucas/catkin_ws/build/mavros/mavros_msgs/catkin_generated/installspace/mavros_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mavros_msgs/cmake" TYPE FILE FILES "/home/lucas/catkin_ws/build/mavros/mavros_msgs/catkin_generated/installspace/mavros_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mavros_msgs/cmake" TYPE FILE FILES
    "/home/lucas/catkin_ws/build/mavros/mavros_msgs/catkin_generated/installspace/mavros_msgsConfig.cmake"
    "/home/lucas/catkin_ws/build/mavros/mavros_msgs/catkin_generated/installspace/mavros_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/mavros_msgs" TYPE FILE FILES "/home/lucas/catkin_ws/src/mavros/mavros_msgs/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/mavros_msgs" TYPE DIRECTORY FILES "/home/lucas/catkin_ws/src/mavros/mavros_msgs/include/mavros_msgs/" FILES_MATCHING REGEX "/[^/]*\\.h$")
endif()

