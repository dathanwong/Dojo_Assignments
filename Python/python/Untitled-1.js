// Write a function that, when passed a string, determines whether or not the 
// parentheses in the string are in a valid configuration


// EXAMPLE: parensValid("I think (it's spring)") would be valid, because the closing
// parentheses comes after the open parentheses.
// parensValid("I don't ) know how these work") would be invalid, because there is no
// open parentheses prior to the closing parentheses
// function parensValid(string){

    //go through the string by each character
    //x Make sure first paren is open
    //if we see a open paren then increment counter by 1
    //if we see closed paren then decrement counter by 1
    //If at the end the counter == 0 then return true
function parensValid(string){
    var counter = 0;
    for (var i = 0; i < string.length; i++){
        if (string[i] === '('){
            counter++;
        }
        else if (string[i] === ')'){
            counter--;
        }
        if (counter == -1){
            return false
        }
    }  
    if (counter == 0){
        return true;
    }
    else{ 
        return false;
    }
}

"I)(t"
counter = 0
i = 1
string[i] = I