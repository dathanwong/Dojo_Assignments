from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def home(request):
    if "id" in request.session:
        return redirect("/wall")
    else:
        return render(request, "home.html")

def createUser(request):
    errors = User.objects.validator(request.POST)
    request.session["firstName"] = request.POST["firstName"]
    request.session["lastName"] = request.POST["lastName"]
    request.session["email"] = request.POST["email"]
    request.session["password"] = request.POST["password"]
    request.session["confirmPassword"] = request.POST["confirmPassword"]
    request.session["birthday"] = request.POST["birthday"]
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = request.POST["password"]
        passwordHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(firstName = request.POST["firstName"], lastName = request.POST["lastName"], email = request.POST["email"], password = passwordHash, birthday = request.POST["birthday"])
        request.session.flush()
        request.session["id"] = user.id
        request.session["name"] = f"{user.firstName} {user.lastName}"
        return redirect("/wall")

def success(request):
    if "id" in request.session:
        return redirect("/wall")
    else:
        return redirect('/')

def login(request):
    request.session.flush()
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        user = User.objects.filter(email = request.POST["email"])
        if user:
            logged_user = user[0]
            request.session.flush()
            request.session['id'] = logged_user.id
            request.session['name'] = f"{logged_user.firstName} {logged_user.lastName}"
            return redirect("/success")
        return redirect("/")  

def logout(request):
    request.session.flush()
    return redirect("/")