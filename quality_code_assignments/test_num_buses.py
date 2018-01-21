import unittest

# I have the same project in PyCharm for the Fundamentals and Crafting Quality Code
# As assignments files have the same name for both courses - a1.py, I put current to a folder
# So, please, remove 'quality_code_assignments.' part to run the module in your environment
from quality_code_assignments.a1 import num_buses

class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_negative(self):
        """Test num_buses with negative value."""

        with self.assertRaises(ValueError):
            num_buses(-1)

    def test_num_buses_zero(self):
        """Test num_buses with zero value."""

        actual = num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_num_buses_upper_bound(self):
        """Test num_buses with upper bound value."""

        actual = num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

    def test_num_buses_lower_bound(self):
        """Test num_buses with lower bound value."""

        actual = num_buses(101)
        expected = 3
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)