#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
print(x)
students[0]['last_name'] = "Bryant"
print(students)
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

#2 Iterate through a list of dictionaries
def iterateDictionary(list):
    for x in range(len(students)):
        print(f"first_name - {students[x]['first_name']}, last_name - {students[x]['last_name']}")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 

#3

def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(f"{some_list[x][key_name]}")

iterateDictionary2('first_name', students)
iterateDictionary2("last_name", students)

#4

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for x in range(len(value)):
            print(value[x])

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)