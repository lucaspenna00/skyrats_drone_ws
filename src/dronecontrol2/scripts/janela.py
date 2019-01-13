#!/usr/bin/env python
# optical flow
from __future__ import print_function

import mavros
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import argparse
import time
from dronecontrol2.msg import Vector3D
from optical_flow import CameraStabilization as camStab


class DroneStabilization:

    def __init__(self, reference_img_topic="/camera1/image_raw"):

        self.image_pub = rospy.Publisher("image_topic_2", Image, queue_size=10)
        self.vel_pub = rospy.Publisher(
            'controle/velocity', Vector3D, queue_size=10)

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber(
            reference_img_topic, Image, self.callback)
        self.stab = camStab()
        self.vec_vel = Vector3D()
        self.vec_vel.x = 0
        self.vec_vel.y = 0
        self.vec_vel.z = 0
        self.pixel_movement = [0, 0]

        self.step = 0

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        (rows, cols, channels) = cv_image.shape
        if not (cols > 60 and rows > 60):  # returns if data have unvalid shape
            return

        precise = self.stab.update(cv_image, precision_cut=1)
        if self.step == 0:
            self.step += 1
        elif self.step == 1:
            self.detectCorners(cv_image)
        elif self.setp == 2:
            pass
        else:
            rospy.shutdown()

            self.step += 1
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            exit()
        elif (k == ord('e')):
            print("erase screen")
            self.stab.clearMask()  # clears all line
        elif (k == ord('r')):
            print("reset features")
            self.stab.resetFeatures(cv_image)

        try:
            # self.vel_pub.publish(self.vec_vel)
            # print(self.vec_vel.x)
            #self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
            pass
        except CvBridgeError as e:
            print(e)

    def detectCorners(self, img):

        features_drift, global_drift = self.stab.getDrift()
        features_pos, global_pos = self.stab.getPosition()

        cv2.imshow("Original topic window", img)
        try:
            self.total_feature_drift += features_drift
        except:
            self.total_feature_drift = features_drift

        print(global_drift.mean())


def main():

    print("init")
    ic = DroneStabilization()
    rospy.init_node('optical_stab', anonymous=True)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
