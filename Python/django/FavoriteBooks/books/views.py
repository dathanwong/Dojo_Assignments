from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import *
from .models import *

# Create your views here.
def books(request):
    if "userID" in request.session:
        context ={
            "user": User.objects.get(id=request.session["userID"]),
            "books": Book.objects.all()
        }
        return render(request, "books.html", context)
    else:
        return redirect("/")

def createBook(request):
    if "userID" in request.session:
        errors = Book.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)
            return redirect("/books")
        user = User.objects.get(id=request.POST["userID"])
        book = Book.objects.create(title=request.POST["title"], description = request.POST["description"], uploaded_by = user)
        book.liked_by.add(user)
        return redirect("/books")
    else:
        return redirect("/")
   

def addFavorite(request, bookID, userID):
    if "userID" in request.session:
        user = User.objects.get(id=userID)
        book = Book.objects.get(id=bookID)
        book.liked_by.add(user)
        return redirect("/books")
    else:
        return redirect("/")

def removeFavorite(request, bookID, userID):
    if "userID" in request.session:
        if userID == request.session["userID"]:
            user = User.objects.get(id=userID)
            book = Book.objects.get(id=bookID)
            book.liked_by.remove(user)
            return redirect(f"/books/{bookID}")
    else:
        return redirect("/")

def updateBook(request, bookID):
    if "userID" in request.session:
        errors = Book.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)
            return redirect(f"/books/{bookID}")
        book = Book.objects.get(id=bookID)
        book.title = request.POST["title"]
        book.description = request.POST["description"]
        book.save()
        return redirect(f"/books/{bookID}")
    else:
        return redirect("/")

def bookInfo(request, bookID):
    if "userID" in request.session:
        context = {
            "book": Book.objects.get(id=bookID),
            "user": User.objects.get(id=request.session["userID"])
        }
        return render(request, "bookInfo.html", context)
    else:
        return redirect("/")

def deleteBook(request, bookID):
    if "userID" in request.session:
        Book.objects.get(id=bookID).delete()
        return redirect("/books")
    else:
        return redirect("/")

def favorites(request):
    if "userID" in request.session:
        user = User.objects.get(id = request.session["userID"])
        context = {
            "user": user,
            "books": user.liked_books.all()
        }
        return render(request, "favorites.html", context)
    else:
        return redirect("/")