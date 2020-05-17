from django.db import models
import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData["title"])<2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData["network"]) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData["desc"]) < 10 and len(postData["desc"]) > 0:
            errors["desc"] = "Description should be at least 10 characters"
        date1 = datetime.datetime.now()
        date2 = datetime.datetime.strptime(postData["releaseDate"], "%Y-%m-%d")
        if date2 > date1:
            errors["date"] = "Release date must be in the past"
        if "id" in postData:
            titleMatch = Show.objects.filter(title=postData["title"]).exclude(id=postData["id"])
        else:
            titleMatch = Show.objects.filter(title=postData["title"])
        if len(titleMatch) > 0:
            errors["titleMatch"] = "Show with the same title already exists in the database"
        return errors

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    releaseDate = models.DateField()
    desc = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()