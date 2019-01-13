# Set Manual Flight Mode
#!/usr/bin/env python

import rospy
from mavros_msgs import srv
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import State
import time

def manual_flight_mode():

	rospy.init_node('manual_flight_mode')
    
    rospy.loginfo('Setting MANUAL Flight Mode')
    
    rate = rospy.Rate(20) # 10hz

    set_mode = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)

    if drone_state != "MANUAL":
    
        rospy.loginfo("SETTING MANUAL FLIGHT MODE")
    
        set_mode("MANUAL")

    else:
    
        return "done"

if __name__ == "__main__":
    
    manual_flight_mode()
