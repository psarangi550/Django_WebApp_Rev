from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=name)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    pages = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('url-name', kwargs={'slug':self.slug})
