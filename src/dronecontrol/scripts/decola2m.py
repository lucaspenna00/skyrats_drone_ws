#!/usr/bin/env python

import rospy

import mavros_msgs

from sensor_msgs.msg import BatteryState

from mavros_msgs import srv # importando services da omavros

from geometry_msgs.msg import PoseStamped

from mavros_msgs.msg import State # importando classe State da Mavros

# ================= Criacao dos objetos ============================ #

goal_pose = PoseStamped()
current_state = State()
battery = BatteryState()

# =============== Criacao das Funcoes ============================= #

voltage = 0.0
current = 0.0
percentage = 0.0

# ================================================================= #

def set_position(x, y, z):
    global goal_pose
    goal_pose.pose.position.z = z
    goal_pose.pose.position.y = y
    goal_pose.pose.position.x = x
    local_position_pub.publish(goal_pose)

def state_callback(state_data):
    global current_state
    current_state = state_data

def callback_battery_status(bateria):
	global voltage
	global current
	global percentage

	voltage = bateria.voltage 
	current = bateria.current
	percentage = bateria.percentage

# =============== Inicializacao do No e Setup dos topicos =============== #

rospy.init_node('Vel_Control_Node', anonymous=True)

rate = rospy.Rate(20)  # publish at 20 Hz

local_position_pub = rospy.Publisher(
	'/mavros/setpoint_position/local', PoseStamped, queue_size=10)

state_status_subscribe = rospy.Subscriber(
	'/mavros/state', State, state_callback)

state_battery = rospy.Subscriber('mavros/battery', BatteryState, callback_battery_status)


arm = rospy.ServiceProxy(
	'/mavros/cmd/arming', mavros_msgs.srv.CommandBool)

set_mode = rospy.ServiceProxy(
	'/mavros/set_mode', mavros_msgs.srv.SetMode)

set_position(0,0,0)

for i in range(300):
  
    local_position_pub.publish(goal_pose)
  
    rate.sleep()

rospy.loginfo("[ ROS] SETUP CONCLUIDO")

# ============================================================================= #

while not rospy.is_shutdown():

# -------- VERIFICAO OFFBOARD E SE ESTA ARMADO --------------- #

	if current_state.mode != "OFFBOARD" or not current_state.armed:
		
		arm(True)

		set_mode(custom_mode="OFFBOARD")

        print(str(current_state.mode))

        if current_state.armed == True:

        	rospy.loginfo("Drone armed")

        if current_state.mode == "OFFBOARD":

            rospy.loginfo('OFFBOARD mode setted')
            
# ------------------------------------------------------------------ #

	set_position(0, 0, 2)

	print ("[ WARN] V = " + str(voltage) +  " , i = "  + str(current) +  " , Remaning = " + str(percentage))

	rate.sleep()
