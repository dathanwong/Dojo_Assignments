from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def random(request):
    if "count" not in request.session:
        request.session["count"] = 1
    else:
        request.session["count"]+= 1
    word = get_random_string(length=14)
    request.session["word"] = word
    return render(request,"random_word.html")

def reset(request):
    request.session["count"] = 0
    return redirect("/random_word")

def submit(request):
    if "count" not in request.session:
        request.session["count"] = 1
    else:
        request.session["count"]+= 1
    word = get_random_string(length=14)
    request.session["word"] = word
    print(request.session["count"])
    return redirect("/random_word")