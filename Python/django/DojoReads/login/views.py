from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def loginPage(request):
    return render(request, "login.html")

def register(request):
    errors = User.objects.registerValidator(request.POST)
    #Store info in session so inputs don't get lost
    request.session["name"] = request.POST["name"]
    request.session["alias"] = request.POST["alias"]
    request.session["email"] = request.POST["email"]
    request.session["password"] = request.POST["password"]
    request.session["confirmPassword"] = request.POST["confirmPassword"]
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
        return redirect("/")
    else:
        #Create user object
        hashedPass = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(name=request.POST["name"], alias = request.POST["alias"], email = request.POST["email"], password = hashedPass)
        #Flush session to remove any stored objects
        request.session.flush()
        #Store user id in session to confirm user is logged in
        request.session["userID"] = user.id
        return redirect("/books")

def login(request):
    errors = User.objects.loginValidator(request.POST)
    #Store info into session so inputs don't get lost
    request.session["loginEmail"] = request.POST["loginEmail"]
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags = key)
        return redirect("/")
    else:
        user = User.objects.filter(email=request.POST["loginEmail"]).first()
        request.session["userID"] = user.id
        return redirect("/books")

def logout(request):
    request.session.flush()
    return redirect("/")