from django.db import models
from django.template.defaultfilters import slugify 

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    counter = models.IntegerField()

    def __str__(self):
        return self.name 
