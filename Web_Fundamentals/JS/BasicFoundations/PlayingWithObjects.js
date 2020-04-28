
var users = [{name: "Michael", age:37}, {name: "John", age:30}, {name: "David", age:27}];
//Print John's age
console.log(users[1].age);

//Print name of first object
console.log(users[0].name);

//Print name and age of each user
for(var user in users){
    console.log(user.name + " - " + user.age);
}