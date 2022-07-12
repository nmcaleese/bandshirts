from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # route for bandshirts index
    path("shirts/", views.shirts_index, name="index"),
    path('shirts/<int:shirt_id>', views.shirts_detail, name='detail'),
]
