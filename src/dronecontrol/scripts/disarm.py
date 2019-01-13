import rospy
import mavros_msgs
from mavros_msgs import srv

arm = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)

for i in range(300):
	arm(False)
