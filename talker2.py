#!/usr/bin/env python
import random
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('chatter1', String, queue_size=10)
rospy.init_node('talker2', anonymous=True)
rate = rospy.Rate(0.3) # 10hz
a=['Rock','Sissors','Paper']
while not rospy.is_shutdown():
    choiceList = random.choice(a)
    hello_str = "%s"  %choiceList
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()