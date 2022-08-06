from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from .models import Employee
from django.db.models import F


# Create your views here.
class HomeTemp(TemplateView):
    template_name = "core/home.html"
    content_type = "text/html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["emps"] = Employee.objects.all()
        return context


class HomeRedirect(RedirectView):
    # url="<url>"
    pattern_name = "core:dest"
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        emp = get_object_or_404(Employee, pk=kwargs["id"])
        emp.counter = F("counter") + 1
        emp.save()
        emp.refresh_from_db()
        return super().get_redirect_url(*args, **kwargs)


class HomeDest(TemplateView):
    template_name = "core/emp.html"
    content_type = "text/html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(kwargs)
        # context["emp"] = Employee.objects.get(pk=kwargs.get("id"))
        context["emp"] = get_object_or_404(Employee,pk=kwargs["id"])
        return context
