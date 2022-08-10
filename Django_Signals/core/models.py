from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
