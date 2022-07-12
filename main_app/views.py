from django.shortcuts import render
from .models import Shirt

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def shirts_index(request):
    shirts = Shirt.objects.all()
    return render(request, "shirts/index.html", {"shirts": shirts})
