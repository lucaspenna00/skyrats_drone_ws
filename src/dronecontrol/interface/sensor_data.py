#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Range

ultrasound = Range()


def ultrassond_callback(data):
    global ultrasound
    ultrasound.range = data.range

rospy.init_node('range_printer', anonymous=True)
rate = rospy.Rate(20)
ultrasound_sub = rospy.Subscriber('/mavros/distance_sensor/hrlv_ez4_pub', Range, ultrassond_callback)


while not rospy.is_shutdown():
    rospy.loginfo(ultrasound.range)
    rate.sleep()
