from django.db import models


# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Base(models.Model):
    emps = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s",
        related_query_name="%(app_label)s_%(class)ss"
    )

    class Meta:
        abstract = True


class Dept(Base):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
