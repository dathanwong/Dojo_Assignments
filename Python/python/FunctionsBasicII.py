#1. Countdown
#Accept number as input return list that counts down by one from that number to 0
def countdown(num):
    output = []
    for i in range(num,-1,-1):
        output.append(i)
    return output

print(countdown(5))

#2. Print and Return
#Receive list of two numbers, print firt value and return the second
def print_and_return(nums):
    print(nums[0])
    return nums[1]

print(print_and_return([1,2]))

#3 First Plus Length
#accepts a list and returns sum of the first value plust the list length
def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

#4 Values greater than second
#accepts a list and creates a new list containing only the values from the original list taht are greater than its second value, print how many values this is and return the new list, return false if less than 2 items
def values_greater(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output
print(values_greater([5,2,3,2,1,4]))
print(values_greater([3]))

#5
#This length that value
def lengthValue(num1, num2):
    output = []
    for x in range(num1):
        output.append(num2)
    return output
print(lengthValue(4,7))
print(lengthValue(6,2))