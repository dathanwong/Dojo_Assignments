from django.shortcuts import render, redirect
from login.models import *
from .models import *
from django.contrib import messages

# Create your views here.
def books(request):
    if "userID" in request.session:
        #get user object
        reviews = Review.objects.all().order_by("-created_at")
        reviews = [reviews[0], reviews[1], reviews[2]]
        context = {
            "user": User.objects.get(id=request.session["userID"]),
            "reviews": reviews,
            "books": Book.objects.all()
        }
        return render(request, "books.html", context)
    else:
        return redirect("/")
    
def addBooksPage(request):
    if "userID" in request.session:
        user = User.objects.get(id=request.session["userID"])
        context = {
            "user": user,
            "authors": Author.objects.all()
        }
        return render(request, "addBook.html", context)
    else:
        return redirect("/")

def createBook(request):
    errors = Book.objects.validator(request.POST)
    errors.update(Author.objects.validator(request.POST))
    errors.update(Review.objects.validator(request.POST))
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/books/add")
    else:
        if "userID" in request.session:
            user = User.objects.get(id = request.session["userID"])
            #Create author if new author created else use author from the list
            if len(request.POST["newAuthor"]) > 0:
                author = Author.objects.create(name=request.POST["newAuthor"])
            else:
                author = Author.objects.get(id = request.POST["authorList"])
            #Create the book
            book = Book.objects.create(title = request.POST["title"], author = author)
            #Create review
            Review.objects.create(review=request.POST["review"], rating=request.POST["rating"], user=user, book=book)
            return redirect(f"/books/{book.id}")

def bookPage(request, bookID):
    if "userID" in request.session:
        book = Book.objects.get(id=bookID)
        reviews = book.reviews.all().order_by("-created_at")
        context = {
            "book": book,
            "reviews": reviews
        }
        return render(request, "bookPage.html", context)
    else:
        return redirect("/")

def addReview(request, bookID):
    if "userID" in request.session:
        book = Book.objects.get(id=bookID)
        user = User.objects.get(id=request.session["userID"])
        Review.objects.create(review=request.POST["review"], rating= request.POST["rating"], book=book, user=user)
        return redirect(f"/books/{bookID}")
    else:
        return redirect("/")

def deleteReview(request, reviewID, bookID):
    if "userID" in request.session:
        review = Review.objects.get(id=reviewID)
        #make sure user owns the review before deleting
        if review.user.id == request.session["userID"]:
            review.delete()
        return redirect(f"/books/{bookID}")
    else:
        return redirect("/")