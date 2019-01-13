#!/usr/bin/env python

import rospy
import mavros_msgs
from mavros_msgs import srv
from geometry_msgs.msg import PoseStamped, TwistStamped
from mavros_msgs.msg import State
import time
import math

goal_pose = PoseStamped() #Possicao que voce deseja ir
local = PoseStamped() #capta a posicao q vc esta
Glocal = PoseStamped() #variavel que recebe a posicao q esta e usaremos para comparacoes
current_state = State() #recebe o estado da maquina

#set_posicao recebe de parametros a posicao que deseja ir e publicara
def set_position(x, y, z):
    global goal_pose
    goal_pose.pose.position.x = x
    goal_pose.pose.position.y = y
    goal_pose.pose.position.z = z
    local_position_pub.publish(goal_pose)

#state_callback subscrevera e recebera o status do DRONE
def state_callback(state_data):
    global current_state
    current_state = state_data

#local_callback subscrevera e recebera a localizacao atual do DRONE
def local_callback(local):
    global Glocal
    Glocal.pose.position.x = local.pose.position.x
    Glocal.pose.position.y = local.pose.position.y
    Glocal.pose.position.z = local.pose.position.z

rospy.init_node('Vel_Control_Node', anonymous = True)

rate = rospy.Rate(20)

#Definicao dos publishers e subscribers
local_position_pub = rospy.Publisher('/mavros/setpoint_position/local', PoseStamped, queue_size = 100)

local_atual = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, local_callback)

state_status_subscribe = rospy.Subscriber('/mavros/state', State, state_callback)

state_publisher = rospy.Publisher('mavros/state', State, queue_size = 100)

arm = rospy.ServiceProxy('/mavros/cmd/arming', mavros_msgs.srv.CommandBool)

set_mode = rospy.ServiceProxy('/mavros/set_mode', mavros_msgs.srv.SetMode)

for i in range(300):
    local_position_pub.publish(goal_pose)
    rate.sleep()

#funcoes de implementacao para movimento
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


def velAng(r):
    T = 60; #constante arbitriarai de teste q na verdade
    #e calculada pela divisao do comprimento do circunferencia
    #pela velocidade do drone
    return 2*math.pi/T


def fazCirculo(R):
    #vaiPara(0,0,0)
    part = 0.1
    i=0
    while(i<500):
        print("LOOP ETERNO")
        theta = (3/4)*math.pi + part
        set_position(R*math.cos(theta), R + R*math.sin(theta), 2)
        part = part + 0.06
        i = i + 1
        rate.sleep()

h = input('Entre com a altura:')
r = 1
x = 0

rospy.loginfo('[ROS] SETUP CONCLUIDO')

while not rospy.is_shutdown():
    if current_state != "OFFBOARD" or not current_state.armed:
        arm(True)
        set_mode(custom_mode = "OFFBOARD")

    print(str(current_state.mode))

    if current_state.armed == True:
        rospy.loginfo("DRONE ARMED")

    if current_state.mode == "OFFBOARD":
        rospy.loginfo('OFFBOARD mode setted')

    fazCirculo(2)
    vaiPara(0,0,0)
    state = State()
    for i in range(300):
        arm(False)
    # vaiPara(r*math.cos(x), r*math.sin(x), h)
    break
    rate.sleep()

    # if compara(Glocal, goal_pose):
    #     while True:
    #         set_position(r*cos(x),r*sin(x), h)
