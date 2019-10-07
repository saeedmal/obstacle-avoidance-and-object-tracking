#! /usr/bin/env python2

import rospy
# from nav_msgs.msg import Odometry
# import tf
# from geometry_msgs.msg import Point, Twist
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np
from random import *
import math


arrmin=1000

def callback(msg):
    global arrmin
    arrmin=min(np.array(msg.ranges))



global cmdvel
rospy.init_node("evade_node")
subsc=rospy.Subscriber("/base_scan", LaserScan, callback)
publ=rospy.Publisher("/cmd_vel",Twist, queue_size=1)    
cmdvel=Twist()
cmdvel.linear.x=2.0
cmdvel.angular.z=0.0
while not rospy.is_shutdown():
    
#     subsc=rospy.Subscriber("/base_scan", LaserScan, callback)
     if arrmin > 0.8:
         cmdvel.linear.x=2.0
         cmdvel.angular.z=0.0
     else:
         cmdvel.linear.x=0.0
         cmdvel.angular.z=0.05

     print(arrmin)
     publ.publish(cmdvel)
     print(repr(cmdvel.linear.x))
#     rospy.spin()

