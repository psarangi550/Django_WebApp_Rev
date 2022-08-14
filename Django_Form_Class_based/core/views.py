from django.shortcuts import render
from .models import Book
from .form import BookModelForm
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify


class BookListView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = "book"


class BookDetailsView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "book.html"



class AddBookForm(FormView):
    form_class = BookModelForm
    template_name = "form.html"

    # success_url = "home"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.slug = None

    def get_success_url(self):
        return reverse_lazy("BookDetailsView")

    def form_valid(self, form):
        self.slug = slugify(form.cleaned_data.get("name"))
        form.save()
        return super().form_valid(form)
