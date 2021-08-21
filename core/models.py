from django.db import models
from datetime import date, datetime
# Create your models here.

#validaciones??
class ShowsManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['title'])<2:
            errors["title"] = "Title should be at least 2 characters."
        if len(postData['network']) <3:
            errors["network"] = "Network should be at least 3 characters."
        if len(postData['desc']) <10:
            errors["desc"] = "Description must be at least 10 characters."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    desc = models.TextField(null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowsManager()