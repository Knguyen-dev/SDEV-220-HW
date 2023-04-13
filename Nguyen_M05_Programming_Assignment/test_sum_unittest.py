import unittest

"""
The output should be "." which indicates success, and "F" which indicates a failure, or a test had failed. 

It'll tell you that the test_sum_tuple function failed raising an AssertionError since obviously the sums aren't equal. 

Useful since you can see where the error was and what the expected result was

"""


class TestSum(unittest.TestCase):
	
	# Tests if the two sums are equal
	def test_sum(self):
		self.assertEqual(sum([1,2,3]), 6, "Should be 6")
	
	def test_sum_tuple(self):
		self.assertEqual(sum((1,2,2)), 6, "Should be 6")

if __name__ == "__main__":
	unittest.main()