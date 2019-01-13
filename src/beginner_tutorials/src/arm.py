#!/usr/bin/env python
import sys
import roslib #biblioteca básica para uso do ROS
import rospy #Biblioteca para facilitar a interface entre o ROS e Python
import mavros #Biblioteca importante para uso do protocolo MAVLink
from std_msgs.msg import String
from std_msgs.msg import Empty
from mavros_msgs.msg import State
from mavros import command

mavros.set_namespace()
command.arming(True)

if __name__ == "__main__":
    import sys

    rospy.init_node('arm_node', anonymous=True)
