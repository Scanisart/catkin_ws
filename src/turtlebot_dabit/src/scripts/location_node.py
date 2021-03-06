#!/usr/bin/env python

import math
import rospy
from nav_msgs.msg import Odometry

landmarks = []
landmarks.append(("Cube", 0.31, -0.99));
landmarks.append(("Blockage", -2.55, -0.89));
landmarks.append(("Cylinder", -1.14, -2.89));
landmarks.append(("Bin", 0.11, -2.42));

def distance(x1, y1, x2, y2):
    xd = x1 - x2
    yd = y1 - y2
    return math.sqrt(xd*xd + yd*yd)

def callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    #rospy.loginfo('x: {}, y: {}'.format(x,y))
    closest_name = None
    closest_distance = None
    for l_name, l_x, l_y in landmarks:
        dist = distance(x, y, l_x, l_y)
        if closest_distance is None or dist < closest_distance:
            closest_name = l_name
            closest_distance = dist
        rospy.loginfo('closest: {}'.format(closest_name))

def main():
    rospy.init_node('location_monitor')
    rospy.Subscriber("/odom", Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
