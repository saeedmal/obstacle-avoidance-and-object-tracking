#!/usr/bin/env python2

import roslib
import rospy
import tf
from geometry_msgs.msg import Twist
import math

#            (trans,rot) = listener.lookupTransform('/robot_1','/robot_0',rospy.Time.now())

#        try:
#            (trans,rot)=listener.waitForTransform("/robot_1", "/robot_0",rospy.Time(), rospy.Duration(1.0))
#        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
#            continue
   
    
if __name__ == '__main__':
    rospy.init_node('pursue_node') #same as tf_listener in tutorials
    turtle_vel = rospy.Publisher('/robot_1/cmd_vel', Twist,queue_size=1)
    listener = tf.TransformListener()
    rospy.sleep(5.0)
    rate = rospy.Rate(1.0)
    while not rospy.is_shutdown():
        now = rospy.Time.now()
        listener.waitForTransform('/robot_1', '/robot_0', now, rospy.Duration(4.0))
        (trans,rot) = listener.lookupTransform('/robot_1', '/robot_0', now)
        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        cmd=Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        turtle_vel.publish(cmd)
        rate.sleep()
