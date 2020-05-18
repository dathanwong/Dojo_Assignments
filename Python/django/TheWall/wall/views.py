from django.shortcuts import render, redirect
from datetime import datetime, timedelta, timezone
from app.models import *
from .models import *
# Create your views here.
def wall(request):
    if not "id" in request.session:
        return redirect("/")
    else:
        user = User.objects.get(id=request.session["id"])
        date = datetime.now(timezone.utc) - timedelta(minutes=30)
        context = {
            "user": user,
            "messages": Message.objects.all().order_by("-created_at"),
            "comments": Comment.objects.all().order_by("created_at"),
            "date": date
        }
        return render(request, "wall.html", context)
    

def logout(request):
    request.session.flush()
    return redirect("/")

def createMessage(request):
    Message.objects.create(message = request.POST["message"], user = User.objects.get(id=request.POST["userID"]))
    return redirect("/wall")

def createComment(request):
    Comment.objects.create(comment = request.POST["comment"], user = User.objects.get(id=request.POST["userID"]), message = Message.objects.get(id=request.POST["messageID"]))
    return redirect("/wall")

def deleteMessage(request, messageID):
    message = Message.objects.get(id=messageID)
    date = datetime.now(timezone.utc) - timedelta(minutes=30)
    if message.created_at > date:
        Message.objects.get(id=messageID).delete()
    return redirect("/wall")