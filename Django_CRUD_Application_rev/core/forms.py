from django import forms
from .models import Equipment


class EquipForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = "__all__"
        widgets = {
            "cp_number": forms.TextInput(attrs={"class": "form-control border-sm-2", "placeholder": "Enter CP"}),
            "sne_id": forms.TextInput(attrs={"class": "form-control border-sm-2", "placeholder": "Enter SNE"}),
            "trs_area": forms.TextInput(attrs={"class": "form-control border-sm-2", "placeholder": "Enter TRS"})
        }
        labels = {
            "cp_number": "CP NUMBER",
            "sne_id":"SNE ID",
            "trs_area": "TRS AREA"
        }
