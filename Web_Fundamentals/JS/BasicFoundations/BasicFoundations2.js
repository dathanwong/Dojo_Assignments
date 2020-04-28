//1. Biggie Size
//Change all positive numbers to string 'big'
function big(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            arr[i] = 'big';
        }
    }
    return arr;
}

//2. Print low return high
//print lowest value in array and return highest value
function lowHigh(arr){
    var min = arr[0];
    var max = arr[0];
    for(var i = 0; i < arr.length; i++){
        if(min > arr[i]){
            min = arr[i];
        }
        if(max < arr[i]){
            max = arr[i];
        }
    }
    console.log(min);
    return max;
}

//3. Print ONe, Return another
//print second to last value in array and return first odd value
function printReturn(arr){
    console.log(arr[arr.length-2]);
    for(var i = 0; i < arr.length; i++){
        if(arr[i]%2 == 1){
            return arr[i];
        }
    }
}

//4. Double Vision
//Double all elements in array
function double(arr){
    var output = [];
    for(var i = 0; i < arr.length; i++){
        output.push(arr[i]*2);
    }
    return output;
}

//5. Count Positives
//replace last value in array with number of positive values found
function countPos(arr){
    var count = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > 0) count++;
    }
    arr[arr.length-1] = count;
    return arr;
}

//6. Evens and odds
//print 'that's odd' when there are 3 odds in a row and print 'Even more so!' when there are 3 evens
function evenOdd(arr){
    var oddCount = 0;
    var evenCount = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i]%2 == 0){
            oddCount = 0;
            evenCount++;
        }
        if(arr[i]%2 == 1){
            evenCount = 0;
            oddCount++;
        }
        if(evenCount == 3){
            console.log("Even more so!");
        }
        if(oddCount == 3){
            console.log("That's Odd")
        }
    }
}

//7. Increment the seconds
//Given array add 1 to every other element and console.log each value and return arr
function incSecond(arr){
    for(var i = 0; i < arr.length; i++){
        if(i%2==1){
            arr[i]++;
        }
        console.log(arr[i]);
    }
    return arr;
}

//8. Previous lenghts
//Replace each string in array with the length of the previous string and return array
function prevLength(arr){
    for(var i = arr.length-1; i >0; i-- ){
        arr[i] = arr[i-1].length;
    }
    return arr;
}

//9. Add Seven
//return a new array equal to original but add 7 to each value
function addSeven(arr){
    var out = [];
    for(var i = 0; i<arr.length; i++){
        out.push(arr[i]+7);
    }
    return out;
}

//10. Reverse Array
//reverse values in place
function reverse(arr){
    for(var i = 0; i < arr.length/2; i++){
        var temp = arr[arr.length-i];
        arr[arr.length-i] = arr[i];
        arr[i] = temp;
    }
    return arr;
}

//11. Outlook Negative
//Make all array values negative
function negative(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i]>0){
            arr[i] = arr[i] * -1;
        }
    }
    return arr;
}

//12. Always Hungry
//Print "yummy" when a value is equal to food, if no "food" print "I'm hungry"
function hungry(arr){
    var count = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] == "food"){
            console.log("yummy");
            count++;
        }
    }
    if(count == 0){
        console.log("I'm hungry");
    }
}

//13. Swap toward center
//swap values on opposite sides of array
function swap(arr){
    for(var i = 0; i <= arr.length/2; i++){
        var temp = arr[i];
        arr[i] = arr[arr.length-i];
        arr[arr.length-i] = temp;
    }
}

//14. scale array
//multiple all numbers by num
function scale(arr, num){
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i] * num;
    }
    return arr;
}