from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def form(request):
    return render(request, "form.html")

def submit(request):
    food = []
    rating = ""
    if "opt" in request.POST:
        food = request.POST.getlist("opt")
    if "rating" in request.POST:
        rating = request.POST["rating"]
    request.session["name"] = request.POST["name"]
    request.session["location"] = request.POST["location"]
    request.session["favLanguage"] = request.POST["favLanguage"]
    request.session["comment"] = request.POST["comment"]
    request.session["rating"] = rating
    request.session["food"] = food
    return redirect('/result')

def result(request):
    return render(request, "result.html")

def back(request):
    return render(request, "form.html")