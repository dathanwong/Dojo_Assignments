import unittest

def reverseList(list):
    if(len(list)<1):
        return False
    for i in range(0,int(len(list)/2),1):
        list[i], list[len(list)-1-i] = list[len(list)-1-i], list[i]
    return list

def isPalindrome(list):
    for i in range(int(len(list)/2)):
        if list[i] != list[len(list)-i-1]:
            return False
    return True

def coins(num):
    output = [0,0,0,0]
    while num >= 25:
        output[0] += 1
        num -= 25
    while num >= 10:
        output[1] += 1
        num -= 10
    while num >= 5:
        output[2] += 1
        num -= 5
    while num >= 1:
        output[3] += 1
        num -= 1
    return output

def factorial(num):
    if(num == 0):
        return 1
    return num*factorial(num-1)

def fibonacci(num):
    if(num == 1 or num == 0):
        return num
    return fibonacci(num-1) + fibonacci(num-2)

class Tests(unittest.TestCase):
    #ReverseList tests
    def testReverseList1(self):
        self.assertEqual(reverseList([1,3,5]),[5,3,1])

    def testReverseList2(self):
        self.assertEqual(reverseList([5,1,4,3]), [3,4,1,5])

    def testReverseList3(self):
        self.assertEqual(reverseList([]), False)

    def testReverseList4(self):
        self.assertEqual(reverseList([0,0,0]), [0,0,0])

    #Palindrome Tests
    def testIsPalindrome1(self):
        self.assertEqual(isPalindrome("racecar"), True)

    def testIsPalindrome2(self):
        self.assertEqual(isPalindrome("rabcr"), False)

    def testIsPalindrome3(self):
        self.assertFalse(isPalindrome("hello"))

    def testIsPalindrome4(self):
        self.assertTrue(isPalindrome("aaaaaa"))

    #Coins tests
    def testCoins1(self):
        self.assertEqual(coins(87), [3,1,0,2])
    def testCoins2(self):
        self.assertEqual(coins(5), [0,0,1,0])
    def testCoins3(self):
        self.assertEqual(coins(100), [4,0,0,0])
    def testCoins4(self):
        self.assertEqual(coins(2), [0,0,0,2])
    def testCoins5(self):
        self.assertEqual(coins(11), [0,1,0,1])

    #Factorial tests
    def testFactorial1(self):
        self.assertEqual(factorial(0), 1)
    def testFactorial2(self):
        self.assertEqual(factorial(5), 120)
    def testFactorial3(self):
        self.assertEqual(factorial(3), 6)

    #Fibonacci tests
    def testFib1(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(4), 3)

if __name__ == '__main__':
    unittest.main()