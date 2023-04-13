import unittest 

from my_sum import sum # import my own functions to test 

from fractions import Fraction # 

# So we can import our functions and code from other files and have a place where we can check
# functionality of the code. We can test simple stuff, and build off of that for our complex stuff
# Hence the name unit test, just verifying if your functions work properly

class TestSum(unittest.TestCase): # Define a test case class 

	# Define a test method to test a list of integers; this method will make some data, and test if 
	# sum is working properly. Finally it defines a command line entry point which runs the main function
	def test_list_int(self):
		# Test that it sums a list of integers
		data = [1,2,3]
		result = sum(data)

		# I know the sum should be six, so I compare the result to 6 to see if something goes wrong
		self.assertEqual(result, 6)

	# Define another test, this time we are expecting it to fail; here we're going to 
	# test the sum() function if it can sum a list of fractions, but we're going to pick an incorrect output
	def test_list_fraction(self):
		# Test that it can sum a list of fractions 
		data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
		result = sum(data)

		# Fraction(9, 10) won't equal 1, so an AssertionError will happen and so the test failed.
		# It shows test_list_fraction, the test that failed, and then __main__.TestSum which is the test case
		# Nice thing it shows you the actual result vs the expected result you put 
		self.assertEqual(result, 1)


# Command-line entry point, meaning that executing test.py on command line will run code at bottom
# Which will in turn runs the tests 
if __name__ == "__main__":
	unittest.main()