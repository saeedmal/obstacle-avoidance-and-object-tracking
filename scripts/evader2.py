#! /usr/bin/env python2

import rospy
from nav_msgs.msg import Odometry
import tf
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

def handle_turtle_pose(msg, turtlename):
    rot=msg.pose.pose.orientation
    posit=msg.pose.pose.position
    br = tf.TransformBroadcaster()
    br.sendTransform((posit.x,posit.y,0.0),(rot.x,rot.y,rot.z,rot.w),rospy.Time.now(),turtlename,"world")
                         
global cmdvel
rospy.init_node("evade_node2")
subsc=rospy.Subscriber("/robot_0/base_scan", LaserScan, callback)
publ=rospy.Publisher("/robot_0/cmd_vel",Twist, queue_size=1)    
cmdvel=Twist()
cmdvel.linear.x=2.0
cmdvel.angular.z=0.0

#turtlename = rospy.get_param('~robot_')
rospy.Subscriber('/robot_0/base_pose_ground_truth',
                     Odometry,
                     handle_turtle_pose,
                     "/robot_0")
rospy.Subscriber('/robot_1/base_pose_ground_truth',
                     Odometry,
                     handle_turtle_pose,
                     "/robot_1")


while not rospy.is_shutdown():
    
#     subsc=rospy.Subscriber("/base_scan", LaserScan, callback)
     if arrmin > 0.8:
         cmdvel.linear.x=2.0
         cmdvel.angular.z=0.0
     else:
         cmdvel.linear.x=0.0
         cmdvel.angular.z=0.5

     print(arrmin)
     publ.publish(cmdvel)
     print(repr(cmdvel.linear.x))
