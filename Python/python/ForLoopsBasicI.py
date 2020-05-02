#1. Print all integers from 0 to 150
for x in range(151):
    print(x)

#2. Multiples of 5
for x in range(5,1001,5):
    print(x)

#3. Counting the dojo way
for x in range(1,101,1):
    if x%10 == 0:
        print("Coding Dojo")
    elif x%5 == 0:
        print("Coding")
    else:
        print(x)
    
#4. Whoa that sucker's huge
sum = 0
for x in range(1,500000,2):
    sum += x
print(sum)
    
#5. Countdown by Fours
for x in range(2018, -1, -4):
    print(x)

#6. Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum+1, 1):
    if x%mult == 0:
        print(x)