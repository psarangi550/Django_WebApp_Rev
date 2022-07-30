from django.urls import path
from .views import paginatedhome

app_name="core"

urlpatterns = [
    path("home/", paginatedhome, name="paginatedhome")
]
