from django.shortcuts import render
from django.core import exceptions
from django.template.response import TemplateResponse
from django.template.response import SimpleTemplateResponse
from django.http import HttpResponse


# Create your views here.

def home(request):
    context = {"data": "hello"}
    temp_resp = TemplateResponse(request, "core/home.html", context=context)
    return temp_resp
