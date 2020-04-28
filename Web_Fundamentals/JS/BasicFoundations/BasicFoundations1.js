//1. Get 1 to 255
//returns an array with all the numbers from 1 to 255
function get1To255(){
    var output = [];
    for(var i = 0; i <= 255; i++){
        output.push(i);
    }
    return output;
}

//2. Get even 1000
//Get the sum of all the even numbers from 1 to 1000
function getEven1000(){
    var output = 0;
    for(var i=2; i <= 1000; i = i+2){
        output += i;
    }
    return output;
}

//3. Sum odd 5000
//Returns the sum of all odd numbers from 1-5000
function sumOdd5000(){
    var output = 0;
    for(var i = 1; i <= 5000; i=i+2){
        output += i;
    }
    return output;
}

//4. Iterate an array
//Returns sum of all values in array
function iterArray(arr){
    var sum = 0;
    for(var i = 0; i < arr.length; i++){
        sum += arr[i];
    }
    return sum;
}

//5. Find max
//Returns max value in array
function findMax(arr){
    var max = arr[0];
    for(var i = 0; i < arr.length; i++){
        if(max < arr[i]){
            max = arr[i];
        }
    }
    return max;
}

//6. Find average
//Return average of array
function getAverage(arr){
    var avg = 0;
    for(var i = 0; i < arr.length; i++){
        avg += arr[i];
    }
    avg = avg/arr.length;
    return avg;
}

//7. Array odd
//Return an array of all odd numbers between 1-50
function arrOdd(){
    var output = [];
    for(var i = 1; i <= 50; i = i+2){
        output.push(i);
    }
    return output;
}

//8. Greater than Y
//Return the number of values greater than Y in an array
function greaterThanY(Y, arr){
    var count = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i]>Y){
            count++;
        }
    }
    return count;
}

//9. Squares
//Return all elements of input array squared
function squares(arr){
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i]*arr[i];
    }
    return arr;
}

//10. Negatives
//Return input array with all negative values replaced with 0
function neg(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0;
        }
    }
    return arr;
}

//11. Max/min/avg
//Given array return an array with [max, min, avg]
function maxMinAvg(arr){
    var max = arr[0];
    var min = arr[0];
    var avg = 0;
    var output = [];
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i];
        }
        if(arr[i] < min){
            min = arr[i];
        }
        avg += arr[i];
    }
    output.push(max);
    output.push(min);
    output.push(avg/arr.length);
    return output;
}

//12. Swap Values
//Swap first and last values of array
function swap(arr){
    var temp = arr[0];
    arr[0] = arr[arr.length-1];
    arr[arr.length-1] = temp;
    return arr;
}

//13. Number to String
//replace negative numbers in array with 'Dojo'
function numToString(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 'Dojo';
        }
    }
    return arr;
}