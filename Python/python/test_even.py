import unittest

def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False

class IsEvenTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(isEven(2), True)
    def testThree(self):
        self.assertEqual(isEven(3), False)
    def setUp(self):
        print("Running SetUp")
    def tearDown(self):
        print("Running TearDown")

if __name__ == "__main__":
    unittest.main()