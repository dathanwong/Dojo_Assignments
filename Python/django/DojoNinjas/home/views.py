from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninjas.objects.all()
    }
    return render(request, "home.html", context)

def addDojo(request):
    Dojo.objects.create(name=request.POST["name"], city = request.POST["city"], state = request.POST["state"])
    return redirect('/')

def addNinja(request):
    Ninjas.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], dojo_id = Dojo.objects.filter(name=request.POST["dojo"])[0])
    return redirect('/')

def deleteDojo(request, dojoId):
    Dojo.objects.get(id=dojoId).delete()
    print(f"Dojo {dojoId} deleted")
    return redirect('/')