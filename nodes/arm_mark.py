#!/usr/bin/env python3

"""
 The arm_mark node draws an end-effector using rviz markers.

PUBLISHERS:
  visualization_marker (visualization_messages/Marker) - The markers we are drawing
  
PARAMETERS:
  period - The amount of time it takes the arm to complete one round
"""

import rospy
import geometry_msgs.msg
from geometry_msgs.msg import Twist, Pose, Point, PoseStamped, Quaternion, Vector3
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import tf2_ros

from visualization_msgs.msg import Marker, InteractiveMarkerControl, MarkerArray

class ArmMark():
    """ Publish visualization_messages/Marker of the arm end-effector
    """
    def __init__(self):
        self.T = rospy.get_param("T")      # initializing the parameter T
        self.pub_marker = rospy.Publisher("visualization_marker", Marker, queue_size = 10)
        self.rate = rospy.Rate(10)
        self.buffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.buffer)
        self.counter = 0

    def draw_marker(self):
        """ draw_marker fanction founds the end-effector position and publish it
        """
        self.marker = Marker()
        self.marker.lifetime = rospy.Duration(self.T/5)
        self.marker.header.frame_id = "link3"
        self.marker.header.stamp = rospy.Time()
        self.marker.id = self.counter
        self.marker.action = Marker.ADD
        self.marker.scale.x = 0.2
        self.marker.scale.y = 0.2
        self.marker.scale.z = 0.2
        if self.x > 0: # marker is a green sphere when x is positive
            self.marker.type = Marker.SPHERE
            self.marker.color.a = 1.0
            self.marker.color.r = 0.0
            self.marker.color.g = 1.0
            self.marker.color.b = 0.0
        else: # marker is a red cube when x is negative
            self.marker.type = Marker.CUBE
            self.marker.color.a = 1.0
            self.marker.color.r = 1.0
            self.marker.color.g = 0.0
            self.marker.color.b = 0.0   
        self.pub_marker.publish(self.marker)
        self.counter += 1

  
    def run(self):
        while not rospy.is_shutdown():
            try:
               # get the latest transform between base_link and link3
               self.trans = self.buffer.lookup_transform("base_link", "link3", rospy.Time())
               self.x = self.trans.transform.translation.x
               rospy.loginfo("Transform is: " + str(self.trans))
               self.draw_marker()  
            except tf2_ros.LookupException as e:
                # the frames don't exist yet
                rospy.loginfo("Lookup exception: " + str(e))
            except tf2_ros.ConnectivityException as e:
                # the tf tree has a disconnection
                rospy.loginfo("Connectivity exception: " + str(e))
            except tf2_ros.ExtrapolationException as e:
                # the times are two far apart to extrapolate
                rospy.loginfo("Extrapolation exception: " + str(e))
            finally:
               self.rate.sleep()


def main():
    """ The main() function. """
    rospy.init_node('arm_mark', log_level = rospy.DEBUG)
    mark = ArmMark()
    mark.run()
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass