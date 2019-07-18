#!/usr/bin/env python

#Important libraries we will be using
import rospy
import cv2
import sys
import numpy as np 
import argparse

#Image specific functions we need
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge() #This makes the bridge that we will be using
frame_rate = 30

def image_handler(ros_image):
    global bridge, frame_rate
    print("Got image")
    image = bridge.imgmsg_to_cv2(ros_image, "bgr8") #Convert to cv type
    cv2.imshow("Original", image)
    cv2.waitKey(1000/frame_rate)

    print(image)
    return

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Subscribe to an image topic")
    parser.add_argument("topic", nargs="+")
    args = parser.parse_args()
    print("The topic is " + args.topic)

    rospy.init_node("image_processor", anonymous=True) 
    #Subscriber to the topic /camera/rgb/image_raw, with type Image, which calls image_handler and passes through the image
    image_sub = rospy.Subscriber(args.topic, Image, image_handler)
    print("Waiting for image")
    try: 
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

