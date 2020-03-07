#!/usr/bin/env python
# license removed for brevity
import rospy
import math
from std_msgs.msg import Float64

def talker():
    pub1 = rospy.Publisher('/threelink/bl2_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('/threelink/bl1_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i=1.0
    while not rospy.is_shutdown():
        position = math.sin(i)
        # position2 = math.sin(i)
        # hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(position)
        pub1.publish(position)
        pub2.publish(position)
        i+=0.1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass