#1. Biggie Size
#Given a list write a function that hanges all positive numbers to big
def biggie(list):
    for x in range(len(list)):
        if list[x] > 0:
            list[x]="big"
    return list
print(biggie([-2,3,5,-5]))

#2. Count Positives
# given a list of numbers replace the last value wiht the number of positive values
def countPos(list):
    count = 0
    for x in range(len(list)):
        if list[x] > 0:
            count += 1
    list[len(list)-1] = count
    return list
print(countPos([-1,1,1,1]))
print(countPos([1,6,-4,-2,-7,-2]))

#3. Sum Total
#Take a list and return the sum of all values in list
def sumTot(list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
    return sum
print(sumTot([1,2,3,4]))
print(sumTot([1,2,3,4]))

#4. Average
# return average of input list
def avg(list):
    sum = 0.0
    for x in range(len(list)):
        sum += list[x]
    return sum/len(list)
print(avg([1,2,3,4]))

#5. Length
#returns length of list
def getLength(list):
    return len(list)
print(getLength([]))

#6. Minimum
#Return minimum value in list return false if empty
def min(list):
    if(len(list)<1):
        return False
    min = list[0]
    for x in range(len(list)):
        if list[x] < min:
            min = list[x]
    return min
print(min([37,2,1,-9]))
print(min([]))

#7 Maximum
#Return max of list, return false if empy
def max(list):
    if(len(list)<1):
        return False
    max = list[0]
    for x in range(len(list)):
        if list[x] > max:
            max = list[x]
    return max
print(max([37,2,1,-9]))
print(max([]))

#8 Ultimate Analysis
#Create function that takes a list and returns dictionary with the sumTotal, average, minimum, maximum, length
def ult(list):
    max = list[0]
    min = list[0]
    sum = 0.0
    for x in range(len(list)):
        if(list[x] > max):
            max = list[x]
        if(list[x]< min):
            min = list[x]
        sum += list[x]
    return {'sumTotal':sum, "average":sum/len(list), "minimum":min, "maximum":max}
print(ult([37,2,1,-9]))

#9 Reverse List
#Take a list and return list with values reveresed without creating a second list
def reverse(list):
    for x in range(len(list)/2):
        temp = list[x]
        list[x] = list[len(list)-1-x]
        list[len(list)-1-x] = temp
    return list
print(reverse([37,2,1,-9,10]))