import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result+=x
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for x in nums:
            self.result-=x
        return self

class Tests(unittest.TestCase):    
    def testAdd1(self):
        self.assertEqual(self.md.add(2).add(2,5,1).subtract(3,2).result, 5)

    def testAdd2(self):
        self.assertEqual(self.md.subtract(4, 1, 6).add(3).result, -8)

    def testAdd3(self):
        self.assertEqual(self.md.add(1,2,3,4,5,6,7).subtract(1,2,3,4,5,6,7).result, 0)

    def setUp(self):
        self.md = MathDojo()


if __name__ == "__main__":
    unittest.main()

# md = MathDojo()

# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x)

# md = MathDojo()
# sub = MathDojo()
# print(md.add(10).add(2).add(15).result)
# print(sub.subtract(14).subtract(12).subtract(1).result)