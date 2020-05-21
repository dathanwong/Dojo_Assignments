from django.db import models
from login.models import *

# Create your models here.
class BookManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["title"]) < 1:
            errors["title"] = "Title cannot be empty"
        return errors

class AuthorManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["authorList"]) < 1 and len(postData["newAuthor"]) < 1 :
            errors["author"] = "Book must have an author"
        return errors

class ReviewManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["review"]) < 1:
            errors["review"] = "Review cannot be empty"
        try:
            rating = int(postData["rating"])
            if not (rating >= 1 and rating <=5):
                errors["rating"] = "Rating must be between 1 and 5"
        except:
            errors["rating"] = "Rating must be between 1 and 5"
        return errors

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
