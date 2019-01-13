# ROS passes around images in its own sensor_msgs/Image message format, but many users will want to use images in conjunction with OpenCV.
#  CvBridge is a ROS library that provides an interface between ROS and OpenCV.

#Converting ROS image messages to OpenCV images:

#To convert a ROS image message into an cv::Mat, module cv_bridge.CvBridge provides the following function:
#cv_image = bridge.imgmsg_to_cv2(image_message, desired_encoding="passthrough")

#Converting OpenCV images to ROS image messages
#convert an cv::Mat into a ROS image message, CvBridge provides the following function:
#image_message = cv2_to_imgmsg(cv_image, encoding="passthrough")
