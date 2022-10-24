# TutorialROS


## start up ros

T1:
roscore
T2:
rosrun turtlesim turtlesim_node
T3:
source ~/catkin_ws/devel/setup.bash
rospack find turtlesim_cleaner

## run

'''rosrun turtlesim_cleaner hitter.py''' 


## executable
chmod u+x ~/catkin_ws/src/turtlesim_cleaner/src/hitter.py
rosrun turtlesim_cleaner hitter.py

## control via arrow keys as in the tutorial with:
'''rosrun turtlesim turtle_teleop_key'''

## after every hit with wall
'''rosservice call /clear'''
