from .models import Book
from django import forms


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ["slug"]

    widgets = [
        {"name": forms.TextInput(attrs={"class": "form-control"})},
        {"author": forms.TextInput(attrs={"class": "form-control"})},
        {"genre": forms.TextInput(attrs={"class": "form-control"})},
        {"page": forms.TextInput(attrs={"class": "form-control"})},
    ]
