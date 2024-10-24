

#!/usr/bin/env python    

import rospy 
from std_msgs.msg import String 

def publisher1(): 

    rospy.init_node('rahul', anonymous=True) 

    
    pub = rospy.Publisher('hello_class', String, queue_size=10) 
    
    rospy.Subscriber("welcome", String)  

    rate = rospy.Rate(2) 
    
    rospy.loginfo('publishing test') 

    while not rospy.is_shutdown(): 
        msg = String() 
        msg.data = "Hello RAA 24_26!" 
        pub.publish(msg) 
        rospy.loginfo(msg)
        rate.sleep() 


if __name__=='__main__':
    try:
        publisher1() 
        
    except rospy.ROSInterruptException: 
        
        pass 
        