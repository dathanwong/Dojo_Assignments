// Given two strings, write an algorithm that will compare and return true or false
// based on whether or not those two strings are the same, ignoring casing
// Example: pYThOn and Python would return true because it's the same word
// with different casing

// HINT: Javascript has .toLowerCase() function built in.
function caseInsensitiveStringCompare(string1, string2) {
    var str1 = string1.toLowerCase();
    var str2 = string2.toLowerCase();
    if(str1 == str2){
        return true;
    }else{
        return false;
    }
}

console.log(caseInsensitiveStringCompare("test","Test"));


// Write a function that takes a string, and returns a reversed version
// of that string. Example: an input of "hello world" would return 
// "dlrow olleh"
function reverse(string) {
    var output ="";
    for(var i = string.length-1; i >=0; i--){
        output += string[i];
    }
    return output;
}

console.log(reverse("hello world"));


// Write a function that takes a string, and returns an acronym.
// Example: "please excuse my dear aunt sally" would return "pemdas"

// HINT: Make note of how you would determine if a letter is the first in a word
function acronyms(string) {
    var output ="";
    if(string[0].match("[a-z]")){
      output += string[0];
    }
    for(var i = 0; i < string.length; i++){
        if(string[i] == " "){
            output += string[i+1];
        }
    }
    return output;
}
console.log(acronyms("please excuse my dear aunt sally"));