from django.shortcuts import render, HttpResponse, redirect
import random, datetime

# Create your views here.
def home(request):
    if "first" not in request.session:
        request.session["first"] = True
        request.session["gold"] = 0
        request.session["events"] = []
    print(request.session["first"])
    print(request.session["gold"])
    print(request.session["events"])
    return render(request, "home.html")

def farm(request):
    message = f"Earned {process(request)} golds from the farm! {getDate()}"
    addEvent(request, message, "green")
    print(request.session["events"])
    return redirect("/")

def cave(request):
    message = f"Earned {process(request)} golds from the cave! {getDate()}"
    addEvent(request, message, "green")
    print(request.session["events"])
    return redirect("/")

def house(request):
    message = f"Earned {process(request)} golds from the house! {getDate()}"
    addEvent(request, message, "green")
    print(request.session["events"])
    return redirect("/")

def casino(request):
    gold = process(request)
    message = ""
    if gold >= 0:
        message = f"Earned {gold} golds from the casino! {getDate()}"
        addEvent(request, message, "green")
    else:
        message = f"Entered a casino and lost {abs(gold)} golds... Ouch.. {getDate()}"
        addEvent(request, message, "red")
    print(request.session["events"])
    return redirect("/")

def process(request):
    gold = int(request.session["gold"])
    randGold = random.randint(int(request.POST["minGold"]), int(request.POST["maxGold"]))
    gold += randGold
    request.session["gold"] = gold
    return randGold

def getDate():
    date = datetime.datetime.now()
    return date.strftime("%Y/%m/%d %I:%M %p")

def addEvent(request, message, color):
    events = request.session["events"]
    events.append({"message":message, "color":color})
    request.session["events"] = events
    return