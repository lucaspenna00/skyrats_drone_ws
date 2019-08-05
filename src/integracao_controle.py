#!/usr/bin/env python

import rospy

import mavros_msgs

from sensor_msgs.msg import BatteryState

from mavros_msgs import srv # importando services da omavros

from geometry_msgs.msg import PoseStamped

from mavros_msgs.msg import State # importando classe State da Mavros

from std_msgs.msg import String

from geometry_msgs.msg import TwistStamped

# ================= Criacao dos objetos ============================ #

goal_pose = PoseStamped()
current_state = State()
battery = BatteryState()
string = String()
velocity_message = TwistStamped()

# =============== Criacao das Variaveis ============================= #

voltage = 0.0
current = 0.0
percentage = 0.0
decision = "zero"
error = 0.1
takeoff_state = False
#currently_x = 0.0
#currently_y = 0.0
#currently_z = 0.0

# ================ Functions definition =========================== #

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

def callback_control_status(command):

    global decision
    decision = command.data

def set_velocity(vel_x, vel_y, vel_z):

    global velocity_message

    velocity_message.twist.linear.x = vel_x
    velocity_message.twist.linear.y = vel_y
    velocity_message.twist.linear.z = vel_z

    vel_pub.publish(velocity_message)

def callback_position_status(rel_position):

    global currently_x
    global currently_y
    global currently_z

    currently_x = rel_position.pose.position.x
    currently_y = rel_position.pose.position.y
    currently_z = rel_position.pose.position.z

# =============== Inicializacao do No e Setup dos topicos =============== #

rospy.init_node('Vel_Control_Node', anonymous=True)

rate = rospy.Rate(20)  # publish at 20 Hz

local_position_pub = rospy.Publisher(
	'/mavros/setpoint_position/local', PoseStamped, queue_size=10)

vel_pub = rospy.Publisher('mavros/setpoint_velocity/cmd_vel', TwistStamped, queue_size=10)

state_status_subscribe = rospy.Subscriber(
	'/mavros/state', State, state_callback)

state_battery = rospy.Subscriber('mavros/battery', BatteryState, callback_battery_status)

control = rospy.Subscriber('controle', String, callback_control_status)

local_position_sub = rospy.Subscriber("mavros/local_position/pose", PoseStamped, callback_position_status)

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

decisao_tomada = False

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

    while (abs(currently_z-1) > error) and (takeoff_state == False):
        set_position(0,0,1)
        rate.sleep()
        print(str(current_state.mode))

    takeoff_state = True

    if decisao_tomada == False:

        set_position(0,0,1)
        rate.sleep()
        print("Aguardando decisao...")

    while decision == 'forward':

        set_velocity(1,0,0)
        rate.sleep()
        print(str(current_state.mode))
        decisao_tomada = True

    while decision == 'back':

        set_velocity(-1,0,0)
        rate.sleep()
        print(str(current_state.mode))
        decisao_tomada = True

    while decision == 'left':

        set_velocity(0,1,0)
        rate.sleep()
        print(str(current_state.mode))
        decisao_tomada = True

    while decision == 'right':

        set_velocity(0,-1,0)
        rate.sleep()
        print(str(current_state.mode))
        decisao_tomada = True

    while decision == 'up':

        set_velocity(0,0,1)
        rate.sleep()
        print(str(current_state.mode))
        decisao_tomada = True

    while decision == 'down':

        set_velocity(0,0,-1)
        rate.sleep()
        print(str(current_state.mode))
        decisao_tomada = True

    while decision == 'stop':

        set_velocity(0,0,0)
        rate.sleep()
        print(str(current_state.mode))
        decisao_tomada = True

    while decision == 'disarm':

        arm(False)

        decisao_tomada = True

        if current_state.armed == False:

            rospy.loginfo("Drone disarm")

            decisao_tomada = True

    while decision == 'returntohome':

        set_position(0,0,0)
        rate.sleep()
        decisao_tomada = True

        if abs(currently_x) < 0.1 and abs(currently_y) < 0.1 and abs(currently_z) < 0.1:

            arm(False)
            break

	print ("[ WARN] V = " + str(voltage) +  " , i = "  + str(current) +  " , Remaning = " + str(percentage))

	rate.sleep()
