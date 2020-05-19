console.log("hello")
$('.error').hide();
$('.register').click(function(){
    var errors = 0;
    
    if($('.firstName').val().length < 2){
        console.log("first name is too short");
        $('.firstNameError').show();
        errors++;
    }
    if($('.lastName').val().length < 2){
        console.log("last name is too short");
        $('.lastNameError').show();
        errors++;
    }
    var date = new Date();
    date.setYear(date.getFullYear()-13);
    if(Date.parse($('.birthday').val()) > Date.parse(date)){
        console.log("You must be at least 13 years old to use this site");
        $('.birthdayError').show();
        errors++;
    }
    if(!$('.email').val().match("^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")){
        console.log("Invalid email address");
        $('.emailError').show();
        errors++;
    }
    if(errors > 0) return false;
})
