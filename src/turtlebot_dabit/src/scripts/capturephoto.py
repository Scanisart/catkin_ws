#!/usr/bin/env python

# Launch gazebo world prior to run this script

from __future__ import print_function
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class CaptureImage:
    def __init__(self):

        self.bridge = CvBridge()
        self.image_received = False

        # Subscribe to the Topic
        img_topic = "/camera/rgb/image_raw"
        self.image_sub = rospy.Subscriber(img_topic, Image, self.callback)
        rospy.sleep(1)

    def callback(self, data):

        # Convert image to OpenCV format
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        self.image_received = True
        self.image = cv_image

    def take_picture(self, img_title):
        if self.image_received:

            cv2.imwrite(img_title, self.image)
            return True
        else:
            return False

if __name__ == '__main__':

    rospy.init_node('capture_photo', anonymous=False)
    camera = CaptureImage()
    img_title = rospy.get_param('~image_title', 'test.jpg')
    if camera.take_picture(img_title):
        rospy.loginfo("Image has been Saved: " + img_title)
    else:
        rospy.loginfo("Image Cannot be Captured")


    rospy.sleep(1)
