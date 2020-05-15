from django.shortcuts import render, HttpResponse, redirect
from .models import *
import datetime

# Create your views here.
def shows(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, "shows.html", context)

def new(request):
    return render(request,"newShow.html")

def create(request):
    newShow = Show.objects.create(title=request.POST["title"], network=request.POST["network"], releaseDate = request.POST["releaseDate"], desc = request.POST["desc"])
    return redirect(f"/shows/{newShow.id}")

def showInfo(request, id):
    context = {
        "show": Show.objects.get(id=id)
    }
    return render(request, "showInfo.html", context)

def edit(request, id):
    context = {
        "show": Show.objects.get(id=id),
    }
    return render(request, "editShow.html", context)

def update(request, id):
    show = Show.objects.get(id=id)
    show.title = request.POST["title"]
    show.network = request.POST["network"]
    show.releaseDate = request.POST["releaseDate"]
    show.desc = request.POST["desc"]
    show.save()
    return redirect(f"/shows/{id}")

def destroy(request, id):
    Show.objects.get(id=id).delete()
    return redirect("/shows")