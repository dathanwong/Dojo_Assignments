from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def create_user(request):
    print("Got Post Info.........")
    request.session["name"] = request.POST["name"]
    request.session["email"] = request.POST["email"]
    return redirect("/success")

def success(request):
    return render(request, "success.html")