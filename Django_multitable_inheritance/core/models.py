from django.db import models


# Create your models here.

class ExamCenter(models.Model):
    cname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.cname


class Student(ExamCenter):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

    def __str__(self):
        return self.name
