from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Equipments


# Create your views here.


def paginatedhome(request):
    all_obj = Equipments.objects.all()
    paginator = Paginator(all_obj, 4, allow_empty_first_page=True)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    return render(request, "core/home.html", {"page_obj": page_obj})
