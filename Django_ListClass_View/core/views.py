from django.shortcuts import render
from .models import Book
from django.views.generic.edit import FormView
from django.views.generic.list import ListView


# Create your views here.

class BookList(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "book"
    paginate_by = 2


class BookListGenre(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "book"

    paginate_by = 1

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset().filter(genre=self.kwargs.get("genre"))
