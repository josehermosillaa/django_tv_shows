from django.db import models
from datetime import date, datetime
# Create your models here.

#validaciones??
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors= {}
        if len(postData['title'])<2:
            errors["title"] = "El titulo debe tener almenos 2 caracteres"
        if len(postData['network']) <3:
            errors["network"] = "Network debe tener al menos 3 caracteres"
        if len(postData['desc']) <10:
            errors["desc"] = "La descripcion debe tener al menos 10 caracteres"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    desc = models.TextField(null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()