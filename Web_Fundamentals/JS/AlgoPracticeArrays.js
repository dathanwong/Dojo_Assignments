var testArr = [6,3,5,1,2,4]

//Print value and sum
var sum = 0;
for(i of testArr){
    sum += i;
    console.log("Num " + i + ", Sum " + sum);
}

//Multiply value by it's position
for(i in testArr){
    testArr[i] = i*testArr[i];
}
console.log(testArr);