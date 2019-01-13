#!/usr/bin/env python

import pygame

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import BatteryState
import time

pygame.init()

black = (0,0,0)
white = (255,255,255)
grey = (100,100,100)
darkGreen = (0,30,0)
brightGreen = (100, 200, 100)

FONT = pygame.font.Font("/home/lucas/catkin_ws/src/dronecontrol/interface/STIX-Bold.otf", 18)

display_width = 920
display_height = 720

xshift = 500        # parametro de deslocamento dos centros dos botoes ao x central da tela
controllerY = 550               # Coordenada y do centro dos botoes
controllerCenterX = display_width/2 - 20      #Coordenada x central da tela
buttonSide = 100    #largura da imagem .png dos botoes
rightControllerCenterX = controllerCenterX + xshift - 2*buttonSide      ## Coordenada x do centro dos botoes da direita
rightControllerCenterY = leftControllerCenterY = controllerY            ## Coordenada y do centro dos botoes
leftControllerCenterX = (controllerCenterX - xshift + 2*buttonSide)/2   ## Coordenada x do centro dos botoes da esquerda
shift = 52                              ## Distancia dos botoes ao centro
cam_height = 400
cam_width = 700
cam_pose = (display_width/2 - cam_height/1.2, display_height/2 - cam_height/1.2)
# largura e altura do retangulo para exibicao de dados
dataWidth = 320
dataHeight = 160
dataRect = [(display_width/2 - dataWidth/2), (display_height-dataHeight-20), dataWidth, dataHeight]
#========== Mensagens a serem publicadas no topico rospy ==========
leftMSG = 'left'
rightMSG = 'right'
downMSG = 'down'
upMSG = 'up'
frontMSG = 'forward'
backMSG = 'back'
yawRightMSG = 'yaw-horario'
yawLeftMSG = 'yaw-antihorario'

open('log', 'w').close() # Apaga os dados do log anterior
file = open('log', 'a')
file.write("*********** flight log *************\n")
file.write("Elapsed Time;Position Y;Position Y;Position Z;Voltage;Current\n\n")
init_time = time.time()
last_time = init_time

position = PoseStamped()
battery = BatteryState()

clock = pygame.time.Clock()
mainDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('--Skyrats: eh nois q voa --')



def main():

    class VisualElement:
        def __init__(self, imgName, position):
            self.img = pygame.image.load(imgName)
            self.position = position

        def show(self):
            mainDisplay.blit(self.img, self.position)
            pass

    class Text:
        def __init__(self, text, position):
            pygame.font.init()
            global FONT
            self.surface = FONT.render(str(text), True, brightGreen)
            self.rectangle = self.surface.get_rect()
            self.rectangle.center = position

        def show(self):
        	mainDisplay.blit(self.surface, self.rectangle)


    class Button:
        def __init__(self, imgName, imgPressedName, position, size, msg):
            self.buttonImg = pygame.image.load(imgName)
            self.buttonPressedImg = pygame.image.load(imgPressedName)
            self.buttonPose = position
            self.buttonSize = size
            self.buttonMsg = msg
            self.show()


        def show(self):
            mainDisplay.blit(self.buttonImg, self.buttonPose)

        def active(self):
            mainDisplay.blit(self.buttonPressedImg, self.buttonPose)

        def inside(self):
            position = self.buttonPose
            mousePos = pygame.mouse.get_pos()
            s = self.buttonSize
            x = mousePos[0] - position[0]
            y = mousePos[1] - position[1]
            if (y >= -x and y<= x) and (y >= x - s and y <= s - x):
                return True
            else:
                return False
            pass

        def publishMsg(self):
            pub = rospy.Publisher('controle', String, queue_size=10)
            rospy.init_node('interface', anonymous=True)
            rate = rospy.Rate(20) # 10hz
            str = self.buttonMsg
            pub.publish(str)
            rate.sleep()
            pass

    ##### Publisher subscriber "interface", que publica no topico "controle"
    def publish(str):
        pub = rospy.Publisher('controle', String, queue_size=10)
        rospy.init_node('interface', anonymous=True)
        rate = rospy.Rate(60) # 10hz
        pub.publish(str)
        rate.sleep()

    mainDisplay.fill(grey)
    mousePos = pygame.mouse.get_pos()
    #~/catkin_ws/src/
    #=========== Criando os objetos para os botoes =================#
    upButton = Button('/home/lucas/catkin_ws/src/dronecontrol/interface/media/upbutton.png', '/home/lucas/catkin_ws/src/dronecontrol/interface/media/upbuttonpressed.png', ((leftControllerCenterX), (leftControllerCenterY - shift)), 150, upMSG)
    downButton = Button('/home/lucas/catkin_ws/src/dronecontrol/interface/media/downbutton.png', '/home/lucas/catkin_ws/src/dronecontrol/interface/media/downbuttonpressed.png', ((leftControllerCenterX), (leftControllerCenterY + shift)), 150, downMSG)
    rightButton = Button('/home/lucas/catkin_ws/src/dronecontrol/interface/media/rightbutton.png', '/home/lucas/catkin_ws/src/dronecontrol/interface/media/rightbuttonpressed.png', ((rightControllerCenterX + shift), (rightControllerCenterY)), 150, rightMSG)
    leftButton = Button('/home/lucas/catkin_ws/src/dronecontrol/interface/media/leftbutton.png', '/home/lucas/catkin_ws/src/dronecontrol/interface/media/leftbuttonpressed.png', ((rightControllerCenterX - shift), (rightControllerCenterY)), 150, leftMSG)
    frontButton = Button('/home/lucas/catkin_ws/src/dronecontrol/interface/media/upbutton.png', '/home/lucas/catkin_ws/src/dronecontrol/interface/media/upbuttonpressed.png', ((rightControllerCenterX), (rightControllerCenterY - shift)), 150, frontMSG)
    backButton = Button('/home/lucas/catkin_ws/src/dronecontrol/interface/media/downbutton.png', '/home/lucas/catkin_ws/src/dronecontrol/interface/media/downbuttonpressed.png', ((rightControllerCenterX), (rightControllerCenterY + shift)), 150, backMSG)
    yawRightButton = Button('/home/lucas/catkin_ws/src/dronecontrol/interface/media/rightbutton.png', '/home/lucas/catkin_ws/src/dronecontrol/interface/media/rightbuttonpressed.png', ((leftControllerCenterX + shift), (leftControllerCenterY)), 150, yawRightMSG)
    yawLeftButton = Button('/home/lucas/catkin_ws/src/dronecontrol/interface/media/leftbutton.png', '/home/lucas/catkin_ws/src/dronecontrol/interface/media/leftbuttonpressed.png', ((leftControllerCenterX - shift), (leftControllerCenterY)), 150, yawLeftMSG)
    button_list = {upButton, downButton, rightButton, leftButton, frontButton, backButton, yawRightButton, yawLeftButton}

    frame = VisualElement('/home/lucas/catkin_ws/src/dronecontrol/interface/media/frame.png', (((display_width/2)-((display_height+shift)/2)),0))

    element_list = {frame}

    #============== Inicializacao do subscriber de posicao ===#
    #rospy.init_node("interface_sub", anonymous=True)
    #rate = rospy.Rate(20)
    def pose_callback(data):
        global position
        position.pose.position.x = data.pose.position.x
        position.pose.position.y = data.pose.position.y
        position.pose.position.z = data.pose.position.z
    position_sub = rospy.Subscriber('/mavros/local_position/pose', PoseStamped, pose_callback)
    #==================== BATERIA ======================#
    def battery_callback(bat_dat):
        global battery

        battery.voltage = bat_dat.voltage
        battery.percentage = bat_dat.percentage
        battery.current = bat_dat.current
    battery_subscriber = rospy.Subscriber('/mavros/battery', BatteryState, battery_callback)

    #======== IMAGENS ==========#
    cam_image = pygame.Surface((cam_width,cam_height))

    def img_callback(img):
        global cam_image
        global newImage
        cam_image = pygame.image.fromstring(img.data, (320,240), "RGB")
        cam_image = pygame.transform.scale(cam_image, (cam_width, cam_height))
        mainDisplay.blit(cam_image, cam_pose)

    #============ LOG ===============#
    def log():
        global last_time
        if(time.time()-last_time) > 0.1:
        	file.write(str(time.time() - init_time))
        	file.write(str(position.pose.position.x) + ";")
        	file.write(str(position.pose.position.y) + ";")
        	file.write(str(position.pose.position.z) + ";")
        	file.write(';')
        	file.write(str(battery.voltage))
        	file.write(';')
        	file.write(str(battery.current))
        	file.write('\n')
        	last_time = time.time()



    exit=False
    img_sub = rospy.Subscriber('/camera1/image_raw', Image, img_callback)

    while not exit:
        mousePos = pygame.mouse.get_pos() # Pega posicao do mouse
        mainDisplay.fill(grey)
        pygame.draw.rect(mainDisplay, darkGreen, dataRect)
        #### Mostra os botoes de acordo com a posicao do mouse
        for Button in button_list:
            if Button.inside():
                Button.active()
                mousec = pygame.mouse.get_pressed()
                click = mousec[0]
                if click == 1:
                    Button.publishMsg()
            else:
                Button.show()
        #
        #========= Mostra elementos visuais =========#
        for Element in element_list:
            Element.show()
        #
        position_text = Text("Position: ", (350,550))
        battery_text = Text("Battery Tension: ", (350, 625))
        battery_voltage = Text(battery.voltage, (400, 640))
        battery_text2 = Text("Battery Current:", (350, 660))
        battery_current = Text(battery.current, (400, 680))
        x_pose = Text(position.pose.position.x, (380,570))
        y_pose = Text(position.pose.position.y, (380, 585))
        z_pose = Text(position.pose.position.z, (380, 600))
        position_text.show()
        x_pose.show()
        y_pose.show()
        z_pose.show()
    	battery_text.show()
    	battery_voltage.show()
    	battery_text2.show()
    	battery_current.show()

        for event in pygame.event.get():
            print('entrou no for')
            if event.type == pygame.QUIT:
                exit=True
                file.close()
                publish("stop")
                #====== Botoes!!!  ==========#
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftButton.active()
                    leftButton.publishMsg()
                else:
                    leftButton.show()

                if event.key == pygame.K_RIGHT:
                    rightButton.active()
                    rightButton.publishMsg()
                else:
                    rightButton.show()

                if event.key == pygame.K_UP:
                    frontButton.active()
                    frontButton.publishMsg()
                else:
                    frontButton.show()

                if event.key == pygame.K_DOWN:
                    backButton.active()
                    backButton.publishMsg()
                else:
                    backButton.show()

                if event.key == pygame.K_w:
                    upButton.active()
                    upButton.publishMsg()
                else:
                    upButton.show()

                if event.key == pygame.K_a:
                    yawLeftButton.active()
                    yawLeftButton.publishMsg()
                else:
                    yawLeftButton.show()

                if event.key == pygame.K_s:
                    downButton.active()
                    downButton.publishMsg()
                else:
                    downButton.show()

                if event.key == pygame.K_d:
                    yawRightButton.active()
                    yawRightButton.publishMsg()
                else:
                    yawRightButton.show()
            elif event.type == pygame.KEYUP:
                publish("stop")
            print(event)
        log()
        pygame.display.update()
        clock.tick()
        pygame.event.poll()

if __name__ == "__main__":
    main()
