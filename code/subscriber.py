#!/usr/bin/env python    

import rospy 
from std_msgs.msg import String 

def printer(msg):

    rospy.loginfo("Message received")
    
    rospy.loginfo(msg) 
def lab_subscriber1(): 

    rospy.init_node('RAA24_subnode') 

    sub = rospy.Subscriber("Greetings", String, printer)  

    rospy.spin() 

if __name__=='__main__': 

    lab_subscriber1() 