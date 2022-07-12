from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # route for bandshirts index
    path("shirts/", views.shirts_index, name="index"),
    path('shirts/<int:shirt_id>', views.shirts_detail, name='detail'),
    #new route to create a band shirt
    path('shirts/create/', views.ShirtCreate.as_view(), name='shirts_create'),
    path('shirts/<int:pk>/update/', views.ShirtUpdate.as_view(), name='shirts_update'),
    path('shirts/<int:pk>/delete/', views.ShirtDelete.as_view(), name='shirts_delete'),

]
