from django.shortcuts import render
from django.http import HttpResponse

class Shirt:  # Note that parens are optional if not inheriting from another class
  def __init__(self, band, description, size, color):
    self.band = band
    self.description = description
    self.size = size
    self.color = color

shirts = [
  Shirt('ACDC', 'Back in Black Tour', 'L', 'Black'),
  Shirt('Avril Lavigne', 'Sk8r Boi Tour', 'S', 'Red'),
  Shirt('Bob Dylan', 'Smoking', 'M', 'Grey')
]

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello</h1>")


def about(request):
    return render(request, 'about.html')

def shirts_index(request):
    return render(request, 'shirts/index.html', {'shirts': shirts })
