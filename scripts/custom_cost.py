#!/usr/bin/env python

from ompl.srv import CustomCost, CustomCostResponse
import rospy
import random

def handle_custom_cost(request):
    cost = random.random()
    rospy.loginfo("Returning cost: %f"%cost)
    return cost

def custom_cost_server():
    rospy.init_node('custom_cost_server')
    rospy.Service('custom_cost', CustomCost, handle_custom_cost)
    rospy.loginfo("Ready to compute custom cost.")
    rospy.spin()

if __name__ == "__main__":
    custom_cost_server()
