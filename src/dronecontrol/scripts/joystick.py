
#!/usr/bin/env python

import rospy

from std_msgs.msg import String

##TEM ALGUMA COISA CAGADEX AQUI #####

###  VERIFICAR COMO IMPORTAR A MENSAGEM DO PACKAGE ###

##from dronecontrol2 import Vector3D

def publicaMensagem(hello_str):

    pub = rospy.Publisher('controle', String, queue_size=10)

    rospy.init_node('joystick', anonymous=True)

    rate = rospy.Rate(10) # 10hz

    pub.publish(hello_str)

    rate.sleep()

if __name__ == '__main__':

    try:

		print("Welcome to Drone Joystick! Press -h to help you! Provided by Skyrats and Turing (Polytechnic School of University of Sao Paulo)")

		print("\n\n w = FORWARD   a = LEFT    d = RIGHT    s = BACK \n  z = UP    x = DOWN    c = STOP \n and -h for help")

		while(True):

			key = raw_input()

			if (key == 'w'):

				publicaMensagem("forward")

			if (key == "a"):

				publicaMensagem("left")

			if (key == "d"):

				publicaMensagem("right")

			if (key == "s"):

				publicaMensagem("back")

			if (key == "yh"):

				publicaMensagem("yaw-horario")

			if (key == "ya"):

				publicaMensagem("yaw-antihorario");

			if (key == "z"):

				publicaMensagem("up")

			if (key == "x"):

				publicaMensagem("down")

			if (key == "c"):

				publicaMensagem("stop")

			if (key == "e"):

				publicaMensagem("disarm")

			if (key == "rth"):

				publicaMensagem("returntohome")

			if (key == "-h"):

				print("\n\n w = FORWARD   a = LEFT    d = RIGHT    s = BACK    z = UP    x = DOWN    c = STOP     e = DISARM")
                print("\n  yh = YAW-HORARIO    ya = YAW-ANTIHORARIO    e = DISARMS")


    except rospy.ROSInterruptException:

        pass
