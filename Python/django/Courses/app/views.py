from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "home.html", context) 

def create(request):
    errors = Course.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        Course.objects.create(name=request.POST["name"], desc=request.POST["desc"])
        return redirect("/")

def destroy(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, "removeCourse.html", context)

def delete(request, id):
    Course.objects.get(id=id).delete()
    return redirect("/")