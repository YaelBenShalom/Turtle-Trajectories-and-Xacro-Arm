 
#!/usr/bin/env python3

""" Unit testing add_two """
import rospy
import numpy
import unittest
from homework2.calculations import FigureEight # TODO 

class TestValues(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestValues, self).__init__(*args, **kwargs)
        W = rospy.get_param("parameters/width")    # initializing the width of the figure eight
        H = rospy.get_param("parameters/height")   # initializing the height of the figure eight
        self.T = rospy.get_param("parameters/period")   # initializing the amount of time it takes to complete the figure eight
        self.figure_eight = FigureEight(self.T, H, W)

    def test_equal_values_on_init(self):
        numpy.testing.assert_almost_equal(self.figure_eight.test_output(0), (0, 0, 1.57079632679490, 1.74532925199433, 0, 0, 2.34810035946921, 0), decimal = 2)

    def test_equal_values_after_half_cycle(self):
        numpy.testing.assert_almost_equal(self.figure_eight.test_output(self.T/2), (0, 0, -1.57079632679490, 1.74532925199433, 0, 0, 2.34810035946921, 0), decimal = 2)

if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, "test_valus", TestValues)
