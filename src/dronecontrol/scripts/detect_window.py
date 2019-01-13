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
from dronecontrol.msg import Vector3D


class DetectWindow:

    def __init__(self, reference_img_topic="/camera1/image_raw"):

        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber(
            reference_img_topic, Image, self.callback)

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        (rows, cols, channels) = cv_image.shape
        if not(cols > 60 and rows > 60):
            return
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

        #cv2.imshow("gray", gray)
        """
        ret, thresh = cv2.threshold(gray, 70, 255, 0)
        im2, contours, hierarchy = cv2.findContours(
            thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(cv_image, contours, -1, (0, 255, 0), 3)
            cv2.imshow("lines", cv_image)
        """

        """
        edges = cv2.Canny(gray, 20, 150, apertureSize=3)
        cv2.imshow("edges", edges)
        minLineLength = 100
        lines = cv2.HoughLinesP(image=edges, rho=1, theta=np.pi / 180, threshold=100,
                                lines=np.array([]), minLineLength=minLineLength, maxLineGap=80)
        a, b, c = lines.shape
        for i in range(a):
            cv2.line(cv_image, (lines[i][0][0], lines[i][0][1]),
                     (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)
        cv2.imshow("lines", cv_image)
        """

        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        edged = cv2.Canny(gray, 30, 200)
        # find contours in the edged image, keep only the largest
        # ones, and initialize our screen contour
        (a, cnts, _) = cv2.findContours(edged.copy(),
                                        cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
        screenCnt = None
        # loop over our contours
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)

            # if our approximated contour has four points, then
            # we can assume that we have found our screen
            if len(approx) == 4:
                screenCnt = approx
                break
        try:

            cv2.drawContours(cv_image, cnts[:], -1, (0, 255, 0), 3)
            cv2.imshow("Janela", cv_image)
        except:
            print("erros")

        k = cv2.waitKey(30) & 0xff
        try:
            print("ok")
        except CvBridgeError as e:
            print(e)


def main():

    print("init DetectWindow")
    dw = DetectWindow()
    rospy.init_node('DetectWindow', anonymous=True)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
