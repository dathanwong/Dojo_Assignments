//1. Sigma
function sigma(num){
    var sum = 0;
    for(var i = 1; i <= num; i++){
        sum+=i;
    }
    return sum;
}

//2. Factorial
function factorial(num){
    var fac = 1;
    for(var i = 1; i <= num; i++){
        fac *= i;
    }
    return fac;
}

//3. Fibonacci
function fib(num){
    var val = [0,1];
    for(var i = 2; i <= num; i++){
        val.push(val[i-1] + val[i-2]);
    }
    return val[num];
}

//4. Array: Second to last
function secondLast(arr){
    if(arr.length < 2){
        return null;
    }else{
        return arr[arr.length-2];
    }
}

//5. Nth to Last
function nLast(arr, n){
    if(arr.length < n){
        return null;
    }else{
        return arr[arr.length-n];
    }
}

//6. Array Second largest
function secondLarge(arr){
    if(arr.length < 2){
        return null;
    }else{
        var max = arr[0];
        var index = 0;
        for(var i = 0; i < arr.length; i++){
            if(max < arr[i]){
                max = arr[i];
                index = i;
            }
        }
        arr[index] = -Infinity;
        max = arr[0];
        for(var i = 0; i < arr.length; i++){
            if(max < arr[i]){
                max = arr[i];
            }
        }
        return max;
    }
}

//7. Double Trouble
function dubtrub(arr){
    var output = [];
    for(i of arr){
        output.push(i);
        output.push(i);
    }
    return output;
}

//Fibonnaci recursive
function fibRe(num){
    if(num == 0 || num == 1){
        return num;
    }
    return fibRe(num-1) + fibRe(num-2);
}