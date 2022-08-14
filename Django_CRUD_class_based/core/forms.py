from django import forms  # importing the forms module
from .models import Equipments


class EquipForm(forms.ModelForm):
    class Meta:
        model = Equipments
        fields = ["cp_number", "sne_id", "trs_area"]
        widgets = {
            "cp_number": forms.TextInput(attrs={"class": "form-control"}),
            "sne_id": forms.TextInput(attrs={"class": "form-control"}),
            "trs_area": forms.TextInput(attrs={"class": "form-control"})
        }
