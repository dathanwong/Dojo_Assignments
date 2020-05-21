from django.db import models
import re, bcrypt

# Create your models here.
class UserManager(models.Manager):
    def registerValidator(self, postData):
        errors = {}
        #name validations
        minName = 2
        if len(postData["name"]) < 2:
            errors["name"] = f"Name must be at least {minName} characters"
        #alias validations
        minAlias = 2
        if len(postData["alias"]) < 2:
            errors["alias"] = f"Alias must be at least {minAlias} characters"
        #Make sure alias is not already taken
        elif len(User.objects.filter(alias=postData["alias"])) > 0:
            errors["alias"] = "Alias already taken"
        #email validations
        #valid email format
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):           
            errors['email'] = "Invalid email address"
        #email not already taken
        elif len(User.objects.filter(email=postData["email"])) > 0:
            errors["email"] = "Email already taken"
        #password validations
        if len(postData["password"]) < 8:
            errors["password"] = "Password must be at least 8 characters"
        #password and confirm password match
        elif not (postData["password"] == postData["confirmPassword"]):
            errors["password"] = "Passwords do not match"
        return errors
    
    def loginValidator(self, postData):
        errors = {}
        #Make sure there is a user that matches the email given
        user = User.objects.filter(email = postData["loginEmail"])
        if len(user) < 1:
            errors["invalidPassword"] = "Email or password is incorrect"
        #Make sure password matches what is in the database
        elif not bcrypt.checkpw(postData["loginPassword"].encode(), user.first().password.encode()):
            errors["invalidPassword"] = "Email or password is incorrect"
        return errors 

class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()