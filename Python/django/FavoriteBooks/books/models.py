from django.db import models
from app.models import *

# Create your models here.
class BookManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["description"]) < 5:
            errors["description"] = "Description must be at least 5 characters"
        if len(postData["title"]) < 1:
            errors["title"] = "Title cannot be empty"
        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()