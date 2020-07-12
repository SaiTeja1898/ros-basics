#!/usr/bin/env python
import rospy
from basics.msg import Complex
def callback(msg):
	ret_msg=Complex()
	ret_msg.real=2*msg.real
	ret_msg.imaginary=2*msg.imaginary
	pub.publish(ret_msg)
rospy.init_node('doubler')
pub = rospy.Publisher('double_complex', Complex)
sub = rospy.Subscriber('complex', Complex, callback)
rospy.spin();
