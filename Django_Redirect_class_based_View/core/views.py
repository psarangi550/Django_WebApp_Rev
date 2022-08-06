from django.shortcuts import render, get_object_or_404
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from .models import Book
from django.db.models import F


# Create your views here.

class SourceView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all()
        context["data"] = "Book Contain Data"
        return context


class CounterRedirect(RedirectView):

    pattern_name = "destination"

    # url="/dest/"

    def get_redirect_url(self, *args, **kwargs):
        book = Book.objects.get(pk=kwargs["pk"])
        book.counter = F('counter') + 1
        book.save()
        book.refresh_from_db()
        return super().get_redirect_url(*args, **kwargs)


class DestinationView(TemplateView):
    template_name = "core/dest.html"

    def get_context_data(self, **kwargs):
        book=get_object_or_404(Book,id=kwargs["pk"])
        context = super().get_context_data(**kwargs)
        context["book"] = book
        context["data"] = "Book Contain Data"
        return context
