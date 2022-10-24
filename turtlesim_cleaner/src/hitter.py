#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import std_srvs.srv
from std_msgs.msg import String
from rosgraph_msgs.msg import Log
#from rosgraph_msgs import Log

def green():
    rospy.set_param('/turtlesim/background_r', 0)
    rospy.set_param('/turtlesim/background_g', 100)
    rospy.set_param('/turtlesim/background_b', 0)

def red():
    rospy.set_param('/turtlesim/background_r', 100)
    rospy.set_param('/turtlesim/background_g', 0)
    rospy.set_param('/turtlesim/background_b', 0)
    rospy.ServiceProxy('clear', std_srvs.srv.Empty)


def blue():
    rospy.set_param('/turtlesim/background_r', 0)
    rospy.set_param('/turtlesim/background_g', 0)
    rospy.set_param('/turtlesim/background_b', 100)
    rospy.ServiceProxy('clear', std_srvs.srv.Empty)

def orange():
    rospy.set_param('/turtlesim/background_r', 255)
    rospy.set_param('/turtlesim/background_g', 140)
    rospy.set_param('/turtlesim/background_b', 0)
    rospy.ServiceProxy('clear', std_srvs.srv.Empty)

def callback(data):
    print(data.msg[39:47]) #x
    print(data.msg[51:60])
    y = data.msg[51:60]
    x = data.msg[39:47]
    
    if "y=-" in y: #top
    	red()
    if "y=11" in y: #bot
    	orange()
    if "x=-" in x: #left
    	blue()
    if "x=11" in x: #right
    	green()
    # left blue()
    # right green()
    
    
    #x = float(data.msg[41:50])
    #print(data.msg.find("y="))
    
    
    
    #rospy.loginfo("I heard %s", data.data)

def main():
    # Starts a new node
    #rospy.init_node('robot_cleaner', anonymous=True)
    #velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #vel_msg = Twist()
    
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("/rosout_agg", Log, callback) #or rosgraph_msgs/Log.msg or std_out
    
    rospy.spin()
    
    
    
    #calling is not working
    
    #change_background_color = rospy.ServiceProxy('/clear', Empty)
    

if __name__ == '__main__':
    try:
        #Testing our function
        main()
    except rospy.ROSInterruptException: pass
