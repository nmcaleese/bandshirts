from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Band, Award
from .forms import ShirtForm

# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def bands_index(request):
    bands = Band.objects.all()
    return render(request, "bands/index.html", {"bands": bands})


def bands_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    id_list = band.awards.all().values_list("id")
    awards_band_doesnt_have = Award.objects.exclude(id__in=id_list)
    shirt_form = ShirtForm()
    return render(
        request,
        "bands/detail.html",
        {"band": band, "shirt_form": shirt_form, "awards": awards_band_doesnt_have},
    )


def assoc_award(request, band_id, award_id):
    Band.objects.get(id=band_id).awards.add(award_id)
    return redirect("detail", band_id=band_id)


class BandCreate(CreateView):
    model = Band
    fields = ["band", "description"]
    # success_url = '/bands/'


class BandUpdate(UpdateView):
    model = Band
    fields = ["description"]


class BandDelete(DeleteView):
    model = Band
    success_url = "/bands/"


def add_shirt(request, band_id):
    form = ShirtForm(request.POST)
    if form.is_valid():
        new_shirt = form.save(commit=False)
        new_shirt.band_id = band_id
        new_shirt.save()
    return redirect("detail", band_id=band_id)


class AwardList(ListView):
    model = Award


class AwardDetail(DetailView):
    model = Award


class AwardCreate(CreateView):
    model = Award
    fields = "__all__"


class AwardUpdate(UpdateView):
    model = Award
    fields = "__all__"


class AwardDelete(DeleteView):
    model = Award
    success_url = "/awards/"
