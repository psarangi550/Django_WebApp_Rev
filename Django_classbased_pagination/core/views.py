from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Book


# Create your views here.


class BooksListView(ListView):
    queryset = Book.objects.all()
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.all()[:1]

