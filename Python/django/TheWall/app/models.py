from django.db import models
import re, bcrypt
from datetime import datetime, timedelta

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["firstName"]) < 2:
            errors["firstName"] = "First Name must be at least 2 characters"
        if len(postData["lastName"]) < 2:
            errors["lastName"] = "Last Name must be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid email address"
        if not postData["password"] == postData["confirmPassword"]:
            errors["passwordMatch"] = "Passwords do not match"
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be at least 8 characters"
        date = datetime.now() - timedelta(days=13*365)
        if datetime.strptime(postData["birthday"], "%Y-%m-%d") > date:
            errors["birthday"] = "You must be at least 13 years old to visit this site"
        #Check email
        emails = User.objects.filter(email=postData["email"])
        if len(emails) > 0:
            errors["email"] = "Email address already registered"
        return errors 

    def loginValidator(self, postData):
        errors = {}
        user = User.objects.filter(email = postData["email"])
        if user:
            logged_user = user[0]
            if not bcrypt.checkpw(postData["password"].encode(), logged_user.password.encode()):
                errors["invalidLogin"] = "Username or password is incorrect"
        else:
            errors["invalidLogin"] = "Username or password is incorrect"
        return errors

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confrimPassword = models.CharField(max_length=255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()