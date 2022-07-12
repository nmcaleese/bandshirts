from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shirt

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def shirts_index(request):
    shirts = Shirt.objects.all()
    return render(request, "shirts/index.html", {"shirts": shirts})


def shirts_detail(request, shirt_id):
    shirt = Shirt.objects.get(id=shirt_id)
    return render(request, "shirts/detail.html", {"shirt": shirt})


class ShirtCreate(CreateView):
  model = Shirt
  fields = '__all__'
  # success_url = '/shirts/'

class ShirtUpdate(UpdateView):
  model = Shirt
  fields = ['description', 'size', 'color']

class ShirtDelete(DeleteView):
  model = Shirt
  success_url = '/shirts/'