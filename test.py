#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('speech', String, queue_size = 10)
    rospy.init_node('talker', anonymous = True)
    rate = rospy.Rate(0.5)
    pub.publish("hello")

if __name__ == '__main__':
    talker()
