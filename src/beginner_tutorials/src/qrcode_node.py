#!/usr/bin/env python

import zbar
import rospy
from PIL import Image
import cv2
from std_msgs.msg import String

def qr_code():
    """
    A simple function that captures webcam video utilizing OpenCV. The video is then broken down into frames which
    are constantly displayed. The frame is then converted to grayscale for better contrast. Afterwards, the image
    is transformed into a numpy array using PIL. This is needed to create zbar image. This zbar image is then scanned
    utilizing zbar's image scanner and will then print the decodeed message of any QR or bar code. To quit the program,
    press "q".
    :return:
    """
    pub = rospy.Publisher('qrcode', String, queue_size=10)
    rospy.init_node('qr_code', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    font = cv2.FONT_HERSHEY_SIMPLEX
    capture = cv2.VideoCapture(0)

    while not rospy.is_shutdown():
        # To quit this program press q.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Breaks down the video into frames
        ret, frame = capture.read()

        # Converts image to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Uses PIL to convert the grayscale image into a ndary array that ZBar can understand.
        image = Image.fromarray(gray)
        width, height = image.size
        zbar_image = zbar.Image(width, height, 'Y800', image.tobytes())

        # Scans the zbar image.
        scanner = zbar.ImageScanner()
        scanner.scan(zbar_image)

        for decoded in zbar_image:
            pub.publish(decoded.data)
            rospy.loginfo(decoded.data)
            rate.sleep()
            #cv2.putText(frame, str(decoded.data),(10,100), font, 2,(0,0,0),2,cv2.LINE_AA)

        # Displays the current frame
        cv2.imshow('Current', frame)
	

if __name__ == '__main__':
    try:
        qr_code()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
