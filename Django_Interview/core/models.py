from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    age = models.IntegerField()
    create_at = models.DateField()

    def __str__(self):
        return self.name
