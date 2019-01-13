#!/usr/bin/env python

import math

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

# =============== Criacao das Variaveis ============================= #

voltage = 0.0
current = 0.0
percentage = 0.0
pos_atual_x = 0.0
pos_atual_y = 0.0
pos_atual_z = 0.0
error = 0.1

# ==================================================================== #

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

def callback_position(posicao):

	global pos_atual_x
	global pos_atual_y
	global pos_atual_z
	pos_atual_x = posicao.pose.position.x
	pos_atual_y = posicao.pose.position.y
	pos_atual_z = posicao.pose.position.z

def verification():
	global pos_atual_x
	global pos_atual_y
	global pos_atual_z
	global voltage

	print_battery_status()

	if current_state.mode != "OFFBOARD" or not current_state.armed:
		
		arm(True)

		set_mode(custom_mode="OFFBOARD")

        print("[ INFO ] Current Flight Mode: " + str(current_state.mode))

        if voltage < 11.3:

        	print("[ DANGEROUS ] LOW BATTERY - RETURNING TO HOME ")

        	while(pos_atual_x != 0.0 and pos_atual_y != 0.0 and pos_origem_z != 0.0):

        		print("[ DANGEROUS ] LOW BATTERY - RETURNING TO HOME ")

        		set_position(0,0,0)

        		rate.sleep()

        		if (abs(pos_atual_x) < 0.1 and abs(pos_atual_y) < 0.1 and abs(pos_atual_z) < 0.1):

        			print(" [ WARN ] DRONE DISARMED")
        			arm(False)	

        if current_state.armed == True:

        	print(" [ WARN ] Drone ARMED")

        if current_state.mode == "OFFBOARD":

            print('[ INFO ] OFFBOARD mode setted')

def print_battery_status():

	global voltage, current, percentage

	print ("[ INFO ] V = " + str(voltage) +  " , i = "  + str(current) +  " , Remaning = " + str(percentage))

def print_current_position():

	global pos_atual_x
	global pos_atual_y
	global pos_atual_z

	print("[ INFO ] Posicao X = " + str(pos_atual_x) + " | Posicao Y = " + str(pos_atual_y) + " | Posicao Z = " + str(pos_atual_z))

def do_square(pos_origem_x, pos_origem_y, pos_origem_z, cumprimento):

	print(" [ INFO ] Doing the Square Mission!")

	global pos_atual_x
	global pos_atual_y
	global pos_atual_z
	global error

	while(pos_atual_x != (pos_origem_x + cumprimento)):

		print("[ DEBUG ] Estamos no primeiro Loop")
		set_position(pos_origem_x + cumprimento, pos_origem_y, pos_origem_z)
		verification()
		print_current_position()
		rate.sleep()

		if (abs(pos_atual_x - ( pos_origem_x + cumprimento )) < error):

			break

	while(pos_atual_y != (pos_origem_y + cumprimento)):

		print("[ DEBUG ] Estamos no segundo Loop")
		set_position(pos_origem_x + cumprimento, pos_origem_y + cumprimento, pos_origem_z)
		print_current_position()
		verification()
		rate.sleep()

		if (abs(pos_atual_y -(pos_origem_y + cumprimento)) < error):

			break

	while(pos_atual_x != pos_origem_x):

		print("[ DEBUG ] Estamos no terceiro Loop")
		set_position(pos_origem_x, pos_origem_y + cumprimento, pos_origem_z)
		print_current_position()
		verification() 
		rate.sleep()

		if(abs(pos_atual_x - abs(pos_atual_x - cumprimento)) < error):

			break

	while(pos_atual_y != pos_origem_y):

		print("[ DEBUG ] Estamos no quarto Loop")
		set_position(pos_origem_x, pos_origem_y, pos_origem_z)
		print_current_position()
		verification()
		rate.sleep()

		if(abs(pos_atual_y - abs(pos_atual_y - cumprimento)) < error):

			break

# ======================================================================= #

# =============== Inicializacao do No e Setup dos topicos =============== #

rospy.init_node('Square', anonymous=True)

rate = rospy.Rate(20)  # publish at 20 Hz

local_position_pub = rospy.Publisher(
	'/mavros/setpoint_position/local', PoseStamped, queue_size=10)

local_position_sub = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, callback_position)

state_status_subscribe = rospy.Subscriber(
	'/mavros/state', State, state_callback)

state_battery = rospy.Subscriber('mavros/battery', BatteryState, callback_battery_status)

arm = rospy.ServiceProxy(
	'/mavros/cmd/arming', mavros_msgs.srv.CommandBool)

set_mode = rospy.ServiceProxy(
	'/mavros/set_mode', mavros_msgs.srv.SetMode)

set_position(0,0,0)

for i in range3(300):
  
    local_position_pub.publish(goal_pose)
  
    rate.sleep()

print("[ INFO ] ROS SETUP CONCLUIDO")

print_current_position();

# ============================================================================= #

while not rospy.is_shutdown():

	print_current_position()

	verification()
	
	print_battery_status()

	print(" [ DEBUG ] loop 1 verification")

	while(abs(pos_atual_z - 2) > 0.2):

		print(" [ DEBUG ] loop 2 verification " + str(pos_atual_z))

		set_position(0, 0, 2)
		rate.sleep()
	
	do_square(0,0,2,3)

	rate.sleep()
