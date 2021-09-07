#!/usr/bin/env python3

"""
 The arm_traj node causes the end-effector to track a given trajectory

PUBLISHERS:
  joint_states (sensor_msgs/JointState) - the arm's joint state

PARAMETERS:
  L1 - The length of the first link
  L2 - The length of the second link
  period - The amount of time it takes the arm to complete one round
"""

import rospy
import geometry_msgs.msg
from geometry_msgs.msg import Twist, Pose, Point, PoseStamped, Quaternion, Vector3
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import sympy
from sympy.abc import t
from sympy import symbols, Eq, Function, cos, sin, acos, atan2, solve, sqrt
from math import pi

class ArmTrajectory():
    """ Publish a sensor_msgs/JointState of the calculated joint state at a
    fixed rate 
    """
    def __init__(self):
        self.L1 = rospy.get_param("L1")    # initializing the parameter L1
        self.L2 = rospy.get_param("L2")    # initializing the parameter L2
        self.T = rospy.get_param("T")      # initializing the parameter T
        self.pub_joint_state = rospy.Publisher("joint_states", JointState, queue_size = 10)
        self.rate = rospy.Rate(10)
        self.t = 0
        self.x = 0
        self.y = 0
        self.theta1 = 0
        self.theta2 = 0


    def calculate_trajectory(self, t):
        """ Calculate the end-effector's location (x, y) as a function of t
        """
        h = 2*(self.L1 + self.L2)/3
        self.x = (0.9*cos(2*pi*self.t/self.T)*sqrt((self.L1 + self.L2)**2 - h**2)) # a function for the component x(t) of the trajectory
        self.y = (2*(self.L1 + self.L2)/3) # a function for the component y(t) of the trajectory
        return self.x, self.y


    def inverse_kinematics(self):
        """ inverse kinematics function that gets the end-effector position (x,y)
        and returns the joint state (theta1, theta2).
        Eqations from Lynch, Park, Modern Robotics Chapter 6.

        returns - the joint state (theta1, theta2)
        """
        beta = acos((self.L1**2 + self.L2**2 - self.x**2 - self.y**2)/(2*self.L1*self.L2))
        alpha = acos((self.x**2 + self.y**2 + self.L1**2 - self.L2**2)/(2*self.L1*sqrt(self.x**2 + self.y**2)))
        gamma = atan2(self.y, self.x)
        self.theta1 = sympy.simplify(gamma - alpha)
        self.theta2 = sympy.simplify(pi - beta)

        return self.theta1, self.theta2


    def arm_msg(self):
        """ calculating the joint state using the end-effector location
        calculation function and the inverse kinematics function.

        Returns - the joints state
        """
        self.t = rospy.get_time()
        self.calculate_trajectory(self.t)
        self.inverse_kinematics()
        rospy.logdebug(f"theta: {self.theta1, self.theta2}")
        joints = JointState()
        joints.header.stamp = rospy.Time.now()
        joints.name = ['joint1', 'joint2']
        joints.position = [self.theta1, self.theta2]
        joints.velocity = []
        joints.effort = []

        return joints


    def run(self):
        while not rospy.is_shutdown():
            rospy.logdebug(f"Run Message")
            self.pub_joint_state.publish(self.arm_msg())
            self.rate.sleep()


def main():
    """ The main() function. """
    rospy.init_node('arm_traj', log_level = rospy.DEBUG)
    traj = ArmTrajectory()
    traj.run()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass