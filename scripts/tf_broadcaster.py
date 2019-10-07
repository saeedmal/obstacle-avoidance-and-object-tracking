#!/usr/bin/env python2

import roslib
import rospy
import tf
from geometry_msgs.msg import Twist
import math

def handle_turtle_pose(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.linear.x, msg.linear.y, 0.0),(0.0,0.0,msg.angular.z),rospy.Time.now()- rospy.Duration(1.0),"world")

if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')
    rospy.Subscriber('/robot_0/cmd_vel', Twist, handle_turtle_pose)
    print "test"
    rospy.spin()
