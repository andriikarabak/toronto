import unittest

# I have the same project in PyCharm for the Fundamentals and Crafting Quality Code
# As assignments files have the same name for both courses - a1.py, I put current to a folder
# So, please, remove 'quality_code_assignments.' part to run the module in your environment
from quality_code_assignments.a1 import swap_k

class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_empty(self):
        """Test swap_k with empty list."""

        nums = []
        nums_expected = []

        swap_k(nums, 0)

        self.assertEqual(nums, nums_expected)

    def test_swap_k_one(self):
        """Test swap_k with a list with one element."""

        nums = [9]
        nums_expected = [9]

        swap_k(nums, 0)

        self.assertEqual(nums, nums_expected)

    def test_swap_k_zero(self):
        """Test swap_k with zero k parameter."""

        nums = [1, 3, 5, 78]
        nums_expected = [1, 3, 5, 78]

        swap_k(nums, 0)

        self.assertEqual(nums, nums_expected)

    def test_swap_k_high(self):
        """Test swap_k with k parameter which is higher than len(L) // 2."""

        nums = [1, 7, 5, 9]

        with self.assertRaises(ValueError):
            swap_k(nums, 3)

    def test_swap_k_negative(self):
        """Test swap_k with negative k parameter."""

        nums = [1, 7, 5, 9]

        with self.assertRaises(ValueError):
            swap_k(nums, -1)

    def test_swap_k_bound(self):
        """Test swap_k with k parameter which is exactly len(L) // 2."""

        nums = [15, 4, 6, 98, 11, 4, 5]
        nums_expected = [11, 4, 5, 98, 15, 4, 6]

        swap_k(nums, 3)

        self.assertEqual(nums, nums_expected)

    def test_swap_k_small(self):
        """Test swap_k with k parameter which is 1."""

        nums = [15, 4, 6, 98, 11, 4, 5]
        nums_expected = [5, 4, 6, 98, 11, 4, 15]

        swap_k(nums, 1)

        self.assertEqual(nums, nums_expected)

if __name__ == '__main__':
    unittest.main(exit=False)
