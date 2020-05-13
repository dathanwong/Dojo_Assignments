from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Authors

# Create your views here.
def home(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, "home.html", context)

def addBook(request):
    Book.objects.create(title=request.POST["title"], desc = request.POST["desc"])
    return redirect('/')

def book(request, id):
    missingAuthors = Authors.objects.exclude(books__id=id)
    context = {
        "book" : Book.objects.get(id=id),
        "authors": missingAuthors
    }
    return render(request, "book.html", context)

def addAuthor(request):
    #First check if author already exists
    authors = Book.objects.get(id=request.POST["bookID"]).authors.all()
    authors = authors.filter(id=request.POST["author"])
    if(authors.count() == 0):
        Book.objects.get(id=request.POST["bookID"]).authors.add(request.POST["author"])
    return redirect('/book/'+request.POST["bookID"])

def authors(request):
    context = {
        "authors": Authors.objects.all()
    }
    return render(request, "authors.html", context)

def addNewAuthor(request):
    Authors.objects.create(first_name=request.POST["firstName"], last_name=request.POST["lastName"], notes = request.POST["notes"])
    return redirect('/authors')

def author(request, id):
    missingBooks = Book.objects.exclude(authors__id=id).all()
    context={
        "author": Authors.objects.get(id=id),
        "books": missingBooks
    }
    return render(request, "authorInfo.html", context)

def addBookAuthor(request):
    #First check if book already exists
    books = Authors.objects.get(id=request.POST["authorID"]).books.all()
    books = books.filter(id=request.POST["book"])
    if(books.count() == 0):
        Authors.objects.get(id=request.POST["authorID"]).books.add(request.POST["book"])
    return redirect('/authors/'+request.POST["authorID"])