

#!/usr/bin/env python    

import rospy 
from std_msgs.msg import String 

def publisher1(): 

    rospy.init_node('rahul_pubnode', anonymous=True) 

    
    pub = rospy.Publisher('Greetings', String, queue_size=10) 
    
    
    rate = rospy.Rate(10) 
    
    rospy.loginfo('publishing test') 

    while not rospy.is_shutdown(): 
        msg = String() 
        msg.data = "Hello i am rahul" 
        pub.publish(msg) 
        rospy.loginfo(msg)
        rate.sleep() 


if __name__=='__main__':
    try:
        publisher1() 
        
    except rospy.ROSInterruptException: 
        
        pass 
        