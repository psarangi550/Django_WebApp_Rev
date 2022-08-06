from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=name)
    pages= models.IntegerField()

    def __str__(self):
        return self.name

