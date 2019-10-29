#!/usr/bin/env python

from ompl.srv import CustomCost, CustomCostResponse
import rospy

def handle_static_cost(request):
    cost = 0.1
    rospy.loginfo("Returning cost: %f"%cost)
    return cost

def static_cost_server():
    rospy.init_node('static_cost_server')
    rospy.Service('custom_cost', CustomCost, handle_static_cost)
    rospy.loginfo("Ready to compute static cost.")
    rospy.spin()

if __name__ == "__main__":
    static_cost_server()