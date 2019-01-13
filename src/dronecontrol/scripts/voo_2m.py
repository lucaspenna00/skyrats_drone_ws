#!/usr/bin/env python

import rospy
import mavros_msgs
from mavros_msgs import srv
from geometry_msgs.msg import PoseStamped, TwistStamped
from mavros_msgs.msg import State
from sensor_msgs.msg import BatteryState
import time

goal_pose = PoseStamped()
current_state = State()
local = PoseStamped()
Glocal = PoseStamped()
battery = BatteryState()

h=2

def compara (x,y):
    if (abs(x.pose.position.z - y.pose.position.z) < 0.1) and (abs(x.pose.position.y - y.pose.position.y) < 0.1) and (abs(x.pose.position.x - y.pose.position.x) < 0.1):
        return True
    return False

def vaiPara (x, y, z):
    set_position(x, y, z)

    rate.sleep()

    while not compara(Glocal, goal_pose):
        set_position (x, y, z)

        rate.sleep()



def set_position(x, y, z):
    global goal_pose
    goal_pose.pose.position.x = x
    goal_pose.pose.position.y = y
    goal_pose.pose.position.z = z
    local_position_pub.publish(goal_pose)


def state_callback(state_data):
    global current_state
    current_state = state_data


def local_callback(local):
    global Glocal

    Glocal.pose.position.x = local.pose.position.x
    Glocal.pose.position.y = local.pose.position.y
    Glocal.pose.position.z = local.pose.position.z

def battery_callback(bat_dat):
    global battery
    global file

    battery.voltage = bat_dat.voltage
    battery.percentage = bat_dat.percentage
    battery.current = bat_dat.current
    # file = open('log.log', 'w')
    # #with open('log.log', 'w') as file:
    # file.write(str(battery.voltage))
    # file.write(' ')
    # file.write(str(battery.current))
    # file.write('\n')
    # file.close()





rospy.init_node('Vel_Control_Node', anonymous = True)

rate = rospy.Rate(20)

local_position_pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size = 100)

local_atual = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, local_callback)

state_status_subscribe = rospy.Subscriber('/mavros/state', State, state_callback)

battery_subscriber = rospy.Subscriber('/mavros/battery', BatteryState, battery_callback)

arm = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)

set_mode = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)

for i in range(300):
    local_position_pub.publish(goal_pose)
    rate.sleep()

rospy.loginfo("[ROS] SETUP CONCLUIDO")
file = open('log.csv', 'a')
cfile = open('corrente.csv', 'a')
tfile = open('tensao.csv', 'a')
timefile = open('tempo.csv', 'a')
#file.write("*********** flight log *************\n")
#file.write("Elapsed Time Battery Voltage Battery Current\n\n")
init_time = time.time()
while not rospy.is_shutdown():
    if current_state != "OFFBOARD" or not current_state.armed:
        arm(True)
        set_mode(custom_mode = "OFFBOARD")

    print(str(current_state.mode))

    if current_state.armed == True:
        rospy.loginfo("DRONE ARMED")

    if current_state.mode == "OFFBOARD":
        rospy.loginfo('OFFBOARD mode setted')

    rate.sleep()
    if not compara(Glocal, goal_pose):
        vaiPara(0, 0, h)
    print("Voltage: ", battery.voltage)
    print(battery.percentage*100, "%")
    print("Position: ", Glocal.pose.position.x, Glocal.pose.position.y, Glocal.pose.position.z)

    file.write(str(time.time() - init_time))
    file.write(' ')
    file.write(str(battery.voltage))
    file.write(' ')
    file.write(str(battery.current))
    file.write('\n')
    ###########
    tfile.write(str(battery.voltage))
    tfile.write('\n')
    ###########
    cfile.write(str(battery.current))
    cfile.write('\n')
    ###########
    timefile.write(str(time.time() - init_time) + '\n')
    ################# SEGURANCA ##############
    if battery.percentage == 0.0:
        vaiPara(0,0,0)
        for i in range(300):
            arm(False)
            print("DESARMANDO DRONE")
    rate.sleep()
file.close()
print("Saiu do while")
