# To write a unit test for sum(), just check hte output of the function with a known output you know is true
# This is a test case, which is an assertion and an entry point.
# If it isn't correct, an assertion error should be raised

def test_sum():
    assert sum([1,2,3]) == 6
if __name__ == "__main__":
    test_sum()
    print("Everything passed")