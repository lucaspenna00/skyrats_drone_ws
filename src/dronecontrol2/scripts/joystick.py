#!/usr/bin/env python

import rospy

from geometry_msgs.msg import PoseStamped

from std_msgs.msg import String

from dronecontrol2.msg import Vector3D

def publicaVelocity(x, y, z):

    pub = rospy.Publisher('controle/velocity', Vector3D, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    vec = Vector3D()
    
    vec.x = x
    vec.y = y
    vec.z = z

    pub.publish(vec)
    
    rate.sleep()

def publicaPosition(x, y, z):
    
    pub = rospy.Publisher('controle/position', Vector3D, queue_size=10)

    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

	vec = Vector3D()
	    
	vec.x = x
	vec.y = y
	vec.z = z

	pub.publish(vec)

	rate.sleep()

if __name__ == '__main__':

    try:

	rospy.init_node('joystick', anonymous=True)  

	publicaPosition(2, 2, 2)
	

    except rospy.ROSInterruptException:

        pass
