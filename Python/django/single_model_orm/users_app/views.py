from django.shortcuts import render, HttpResponse, redirect
from .models import User
# Create your views here.
def home(request):
    context = {
        "users": User.objects.all()
    }
    return render(request,"home.html", context)

def addUser(request):
    print(request.POST)
    User.objects.create(first_name=request.POST["firstName"], last_name=request.POST["lastName"], email_address=request.POST["email"], age=request.POST["age"])
    return redirect("/")