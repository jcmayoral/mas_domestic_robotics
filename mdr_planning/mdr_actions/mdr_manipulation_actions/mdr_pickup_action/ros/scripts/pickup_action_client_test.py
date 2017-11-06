#!/usr/bin/env python
import sys
import rospy
import roslib
import actionlib

from mdr_pickup_action.msg import PickUpAction, PickUpGoal

if __name__ == '__main__':
    rospy.init_node('pickup_action_client_test')

    client = actionlib.SimpleActionClient('pickup_server', PickUpAction)
    client.wait_for_server()

    # Fill in the goal here
    goal = PickUpGoal()
    goal.position.header.frame_id = 'base_link'
    goal.position.header.stamp = rospy.Time.now()
    goal.position.point.x = -0.7
    goal.position.point.y = 0.0
    goal.position.point.z = 0.9

    client.send_goal(goal)
    client.wait_for_result()
    rospy.loginfo(client.get_result())
