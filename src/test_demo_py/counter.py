#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

class Counter:

    # Initialize counter
    def __init__(self):
        self.counter_value = 0

    # A method for increasing the counter value
    def increment(self, step):
        self.counter_value += step

    # Method for publishing the counter value to ROS
    def start_publisher(self):
        pub = rospy.Publisher('counter_value', Int32, queue_size=10)
        rospy.init_node('counter', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            rospy.loginfo(self.counter_value)
            pub.publish(self.counter_value)
            self.increment(3)
            rate.sleep()

if __name__ == '__main__':
    try:
        counter = Counter()
        counter.start_publisher()
    except rospy.ROSInterruptException:
        pass
