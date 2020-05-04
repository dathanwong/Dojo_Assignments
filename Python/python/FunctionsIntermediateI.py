import random
def randInt(min=0, max=100):
    if min > max:
        return False
    num = random.random()*max
    return round(num)

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100copy
print(randInt(min=50, max=500))   