 
#!/usr/bin/env python3

""" Unit testing add_two """
import unittest
from homework2.calculations import FigureEight # TODO 

class TestValues(unittest.TestCase):
    W = rospy.get_param("parameters/width")    # initializing the width of the figure eight
    H = rospy.get_param("parameters/height")   # initializing the height of the figure eight
    T = rospy.get_param("parameters/period")   # initializing the amount of time it takes to complete the figure eight
    R = rospy.get_param("~pub_freq")           # initializing the frequency at which to publish the messages
    figure_eight = FigureEight(T, H, W)

    def test_equal_values(self):
        self.assertEquals(figure_eight.test_output(0), (0, 0, 1.57079632679490, 1.74532925199433, 0, 0, 2.34810035946921, 0))

if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, "test_valus", TestValues)
