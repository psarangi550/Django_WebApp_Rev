from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Equipment
from .forms import EquipForm


# Create your views here.

# display and new equipment

def home_view(request):
    if request.method == "POST":
        form = EquipForm(request.POST)
        if form.is_valid():  # validating the form
            form.save()  # saving the form
            form = EquipForm()
    else:
        form = EquipForm()
    equips = Equipment.objects.all()
    return render(request, template_name="core/home.html", context={"form": form, "equips": equips})


# delete and element

def delete_view(request, id):
    if request.method == "POST":
        equip = Equipment.objects.get(id=id)
        equip.delete()
        return HttpResponseRedirect("/home/")
    else:
        return HttpResponseRedirect("/home/")


# update element


def update_view(request, id):
    if request.method == "POST":
        equip = Equipment.objects.get(id=id)
        form = EquipForm(data=request.POST, instance=equip)
        if form.is_valid():
            form.save()
            form = EquipForm(instance=equip)
            return HttpResponseRedirect("/home/")
    else:
        equip = Equipment.objects.get(id=id)
        form = EquipForm(instance=equip)
    return render(request, template_name="core/update.html", context={"form": form})
