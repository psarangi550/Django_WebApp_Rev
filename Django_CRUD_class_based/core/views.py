from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.base import View
from .forms import EquipForm
from .models import Equipments


# Create your views here.
class AddandShowView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = EquipForm()
        equips = Equipments.objects.all()
        context["form"] = form
        context["equips"] = equips
        return context

    def post(self, request, **kwargs):
        form = EquipForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect("/home/")


class EquipUpdateView(View):

    def get(self, request, *args, **kwargs):
        equip = Equipments.objects.get(pk=self.kwargs["pk"])
        form = EquipForm(instance=equip)
        return render(request, "core/update.html", {"form": form})

    def post(self, request, ** kwargs):
        equip = Equipments.objects.get(pk=self.kwargs["pk"])
        form = EquipForm(request.POST,instance=equip)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home/")


class EquipDeleteView(RedirectView):
    url = "/home/"

    def get_redirect_url(self, *args, **kwargs):
        equip = Equipments.objects.get(pk=self.kwargs["pk"])
        equip.delete()
        return super().get_redirect_url(*args, **kwargs)
