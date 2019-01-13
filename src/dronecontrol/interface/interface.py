#!/usr/bin/env python
import pygame
import time

import rospy
from std_msgs.msg import String

## arquivo original com imagens diminuidas por um fator de 2/3

pygame.init()

################################### Parametros ###############################################

display_width = 920

display_height = 720

       #(R,G,B)
black = (0,0,0)

white = (255,255,255)

grey = (100,100,100)

darkGreen = (0,30,0)

xshift = 500        # parametro de deslocamento dos centros dos botoes ao x central da tela

controllerY = 550               # Coordenada y do centro dos botoes

controllerCenterX = display_width/2 - 20      #Coordenada x central da tela

buttonSide = 100    #largura da imagem .png dos botoes

rightControllerCenterX = controllerCenterX + xshift - 2*buttonSide      ## Coordenada x do centro dos botoes da direita

rightControllerCenterY = leftControllerCenterY = controllerY            ## Coordenada y do centro dos botoes

leftControllerCenterX = (controllerCenterX - xshift + 2*buttonSide)/2   ## Coordenada x do centro dos botoes da esquerda

shift = 52                              ## Distancia dos botoes ao centro

# largura e altura do retangulo para exibicao de dados
dataWidth = 320

dataHeight = 160

frame_pos = (((display_width/2)-(766/2)),0)        ## largura da moludura = 800 (altura 600)

##############################################################################################

gameDisplay = pygame.display.set_mode((display_width,display_height))   # Cria a tela

pygame.display.set_caption('--SkyRats--')           ## Nome do programa

clock = pygame.time.Clock()

# Variaveis para armazenar as imagens
upButtonImg = pygame.image.load('media/upbutton.png')
upButtonPressedImg = pygame.image.load('media/upbuttonpressed.png')
downButtonImg = pygame.image.load('media/downbutton.png')
downButtonPressedImg = pygame.image.load('media/downbuttonpressed.png')
rightButtonImg = pygame.image.load('media/rightbutton.png')
rightButtonPressedImg = pygame.image.load('media/rightbuttonpressed.png')
leftButtonImg = pygame.image.load('media/leftbutton.png')
leftButtonPressedImg = pygame.image.load('media/leftbuttonpressed.png')
frameImg = pygame.image.load('media/frame.png')


# Funcoes para mostrar as imagens na tela


def insideButton(x,y,s):

    if (y >= -x and y<= x) and (y >= x - s and y <= s - x):

        return True

    else:

        return False


def frontbutton():
    position = ((rightControllerCenterX), (rightControllerCenterY - shift))
    gameDisplay.blit(upButtonImg, position)
    x = mousePos[0] - position[0]
    y = mousePos[1] - position[1] - buttonSide/2
    if insideButton(x,y,buttonSide) == True:
        gameDisplay.blit(upButtonPressedImg, position)
        mousec = pygame.mouse.get_pressed()
        click = mousec[0]
        if click == 1:
            msg = 'forward'
            publicaMensagem(msg)

def backbutton():
    position = ((rightControllerCenterX), (rightControllerCenterY + shift))
    gameDisplay.blit(downButtonImg, position)
    x = mousePos[0] - position[0]
    y = mousePos[1] - position[1] - 0.5*buttonSide
    if insideButton(x,y,buttonSide) == True:
        gameDisplay.blit(downButtonPressedImg, position)
        mousec = pygame.mouse.get_pressed()
        click = mousec[0]
        if click == 1:
            msg = 'back'
            publicaMensagem(msg)



def rightbutton():
    position = ((rightControllerCenterX + shift), (rightControllerCenterY))
    gameDisplay.blit(rightButtonImg, position)
    x = mousePos[0] - position[0]
    y = mousePos[1] - position[1] - buttonSide/2
    if insideButton(x,y,buttonSide) == True:
        gameDisplay.blit(rightButtonPressedImg, position)
        mousec = pygame.mouse.get_pressed()
        click = mousec[0]
        if click == 1:
            msg = 'right'
            publicaMensagem(msg)


def leftbutton():
    position = ((rightControllerCenterX - shift), (rightControllerCenterY))
    gameDisplay.blit(leftButtonImg, position)
    x = mousePos[0] - position[0]
    y = mousePos[1] - position[1] - buttonSide/2
    if insideButton(x,y,buttonSide) == True:
        gameDisplay.blit(leftButtonPressedImg, position)
        mousec = pygame.mouse.get_pressed()
        click = mousec[0]
        if click == 1:
            msg = ('left')
            publicaMensagem(msg)


def yawrightbutton():
    position = ((leftControllerCenterX + shift), (leftControllerCenterY))
    gameDisplay.blit(rightButtonImg, position)
    x = mousePos[0] - position[0]
    y = mousePos[1] - position[1] - buttonSide/2
    if insideButton(x,y,buttonSide) == True:
        gameDisplay.blit(rightButtonPressedImg, position)
        mousec = pygame.mouse.get_pressed()
        click = mousec[0]
        if click == 1:
            msg = ('yaw-horario')
            publicaMensagem(msg)

def yawleftbutton():
    position = ((leftControllerCenterX - shift), (leftControllerCenterY))
    gameDisplay.blit(leftButtonImg, position)
    x = mousePos[0] - position[0]
    y = mousePos[1] - position[1] - buttonSide/2
    if insideButton(x,y,buttonSide) == True:
        gameDisplay.blit(leftButtonPressedImg, position)
        mousec = pygame.mouse.get_pressed()
        click = mousec[0]
        if click == 1:
            msg = ('yaw-antihorario')
            publicaMensagem(msg)

def upbutton():
    position = ((leftControllerCenterX), (leftControllerCenterY - shift))
    gameDisplay.blit(upButtonImg, position)
    x = mousePos[0] - position[0]
    y = mousePos[1] - position[1] - buttonSide/2
    if insideButton(x,y,buttonSide) == True:
        gameDisplay.blit(upButtonPressedImg, position)
        mousec = pygame.mouse.get_pressed()
        click = mousec[0]
        if click == 1:
            msg = ('up')
            publicaMensagem(msg)

def downbutton():
    position = ((leftControllerCenterX), (leftControllerCenterY + shift))
    gameDisplay.blit(downButtonImg, position)
    x = mousePos[0] - position[0]
    y = mousePos[1] - position[1] - buttonSide/2
    if insideButton(x,y,buttonSide) == True:
        gameDisplay.blit(downButtonPressedImg, position)
        mousec = pygame.mouse.get_pressed()
        click = mousec[0]
        if click == 1:
            msg = ('down')
            publicaMensagem(msg)

def frame():

    gameDisplay.blit(frameImg, frame_pos)


def publicaMensagem(hello_str):

    pub = rospy.Publisher('controle', String, queue_size=10)

    rospy.init_node('interface', anonymous=True)

    rate = rospy.Rate(10) # 10hz

    pub.publish(hello_str)

    rate.sleep()


exit = False

def play_music():

    pygame.mixer.music.load("metropolis.mp3")

    pygame.mixer.music.play()

    time.sleep(180)


import threading

musicThread = threading.Thread(target=play_music)

musicThread.start()

while not exit:

    mousePos = pygame.mouse.get_pos()

    gameDisplay.fill(grey)

    frontbutton()

    backbutton()

    rightbutton()

    leftbutton()

    yawrightbutton()

    yawleftbutton()

    upbutton()

    downbutton()

    frame()

    dataRect = [(display_width/2 - dataWidth/2), (display_height-dataHeight-20), dataWidth, dataHeight]

    pygame.draw.rect(gameDisplay, darkGreen, dataRect)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            exit = True

            # controle com Teclado
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT:

            position = ((rightControllerCenterX - shift), (rightControllerCenterY))

            gameDisplay.blit(leftButtonPressedImg, position)

            msg = ('left')

            publicaMensagem(msg)

        elif event.key == pygame.K_RIGHT:

            position = ((rightControllerCenterX + shift), (rightControllerCenterY))

            gameDisplay.blit(rightButtonPressedImg, position)

            msg = ('right')

            publicaMensagem(msg)

        elif event.key == pygame.K_DOWN:

            position = ((rightControllerCenterX), (rightControllerCenterY + shift))

            gameDisplay.blit(downButtonPressedImg, position)

            msg = ('back')

            publicaMensagem(msg)


        elif event.key == pygame.K_UP:

            position = ((rightControllerCenterX), (rightControllerCenterY - shift))

            gameDisplay.blit(upButtonPressedImg, position)

            msg = ('forward')

            publicaMensagem(msg)


        elif event.key == pygame.K_w:

            position = ((leftControllerCenterX), (leftControllerCenterY - shift))

            gameDisplay.blit(upButtonPressedImg, position)

            msg = ('up')

            publicaMensagem(msg)

        elif event.key == pygame.K_s:

            position = ((leftControllerCenterX), (leftControllerCenterY + shift))

            gameDisplay.blit(downButtonPressedImg, position)

            msg = ('down')

            publicaMensagem(msg)

        elif event.key == pygame.K_d:

            position = ((leftControllerCenterX + shift), (leftControllerCenterY))

            gameDisplay.blit(rightButtonPressedImg, position)

            msg = ('yaw-horario')

            publicaMensagem(msg)

        elif event.key == pygame.K_a:

            position = ((leftControllerCenterX - shift), (leftControllerCenterY))

            gameDisplay.blit(leftButtonPressedImg, position)

            msg = ('yaw-antihorario')

            publicaMensagem(msg)

        pygame.event.poll()

    print(event)
    pygame.display.update()

    clock.tick()
