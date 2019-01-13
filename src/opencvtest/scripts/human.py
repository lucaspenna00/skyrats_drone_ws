#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

class image_converter:

  def __init__(self):
    ##self.image_pub = rospy.Publisher("image_topic_2",Image, queue_size=10)

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/camera1/image_raw", Image , self.callback)

  def callback(self,data):
    try:
      self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)

 #   cv2.imshow("Image window", cv_image)
 #   cv2.waitKey(1)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

#def main(args):
#
#  ic = image_converter()
#  rospy.init_node('image_converter', anonymous=True)
#  try:
#    rospy.spin()
#  except KeyboardInterrupt:
#    print("Shutting down")
#  cv2.destroyAllWindows()

#############################################################################

def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh


def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)


if __name__ == '__main__':

    rospy.init_node('image_converter', anonymous=True)

    ic = image_converter()

    try:
	    hog = cv2.HOGDescriptor()
	    hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
	    cap=cv2.VideoCapture(ic.cv_image)
	    while True:
		_,frame=cap.read()
		found,w=hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)
		draw_detections(frame,found)
		cv2.imshow('feed',frame)
		ch = 0xFF & cv2.waitKey(1)
		rospy.spin()

		if ch == 27:
		    break
	    cv2.destroyAllWindows()

    except KeyboardInterrupt:
    	print("Shutting down")
  	cv2.destroyAllWindows()
