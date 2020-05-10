from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Place holder to display a new form to create a new blog")

def create(request):
    return redirect("/blogs")

def show(request, num):
    return HttpResponse(f"Placeholder to display blog number {num}")

def edit(request, num):
    return HttpResponse(f"Placeholder to edit blog {num}")

def destroy(request, num):
    return redirect("/blogs")