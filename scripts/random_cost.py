#!/usr/bin/env python

from moveit_msgs.srv import CustomCost, CustomCostResponse
import rospy
import random


def handle_random_cost(request):
    cost = random.random()
    rospy.loginfo("Returning cost: %f" % cost)
    srv = CustomCostResponse()
    srv.cost = cost
    srv.type = 0
    return srv


def random_cost_server():
    rospy.init_node('random_cost_server')
    rospy.Service('custom_cost', CustomCost, handle_random_cost)
    rospy.loginfo("Ready to compute random cost.")
    rospy.spin()


if __name__ == "__main__":
    random_cost_server()
