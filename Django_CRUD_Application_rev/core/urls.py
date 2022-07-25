from django.urls import path
from .views import home_view,delete_view,update_view

app_name="core"

urlpatterns = [
    path("home/", home_view, name="home"),
    path("delete/<int:id>/", delete_view,name="deleteview",),
    path("update/<int:id>/", update_view,name="updateview",)
]
