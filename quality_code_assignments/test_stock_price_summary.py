import unittest

# I have the same project in PyCharm for the Fundamentals and Crafting Quality Code
# As assignments files have the same name for both courses - a1.py, I put current to a folder
# So, please, remove 'quality_code_assignments.' part to run the module in your environment
from quality_code_assignments.a1 import stock_price_summary

class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_empty(self):
        """Test stock_price_summary with empty list."""

        actual = stock_price_summary([])
        expected = ()
        self.assertEqual(expected, actual)

    def test_stock_price_summary_zero(self):
        """Test stock_price_summary with a list with only zero values."""

        actual = stock_price_summary([0, 0, 0])
        expected = (0.0, 0.0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_one(self):
        """Test stock_price_summary with a list with only one non-zero value."""

        actual = stock_price_summary([0.14])
        expected = (0.14, 0.0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_general(self):
        """Test general logic of stock_price_summary with a list,
        where absolute values of sums for gains and losses are the same."""

        actual = stock_price_summary([0.01, -0.01, 0.02, -0.02, 0.1, -0.1])
        expected = (0.13, -0.13)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
