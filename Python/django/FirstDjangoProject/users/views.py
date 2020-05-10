from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def register(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(reqeust):
    return HttpResponse("placeholder for users to log in")

def new(request):
    return redirect("/register")

def users(request):
    return HttpResponse("placeholder to later display all the list of users")

def home(request):
    return redirect("/blogs")