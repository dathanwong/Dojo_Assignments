console.log("hello");

$("img").click(function (){
    console.log("Clicked");
    $(this).fadeOut();
})

$("button").click(function(){
    $("img").fadeIn();
})