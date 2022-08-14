from django.db import models


# Create your models here.
class BookManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(BookManager, self).get_queryset(*args, **kwargs).order_by('-id')


class Book(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()
    manager = BookManager()
    objects = models.Manager()

    def __str__(self):
        return self.name

