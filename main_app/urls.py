from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    # route for bands index
    path("bands/", views.bands_index, name="index"),
    path('bands/<int:band_id>', views.bands_detail, name='detail'),
    #new route to create a band
    path('bands/create/', views.BandCreate.as_view(), name='bands_create'),
    path('bands/<int:pk>/update/', views.BandUpdate.as_view(), name='bands_update'),
    path('bands/<int:pk>/delete/', views.BandDelete.as_view(), name='bands_delete'),
    path("bands/<int:band_id>/add_shirt/", views.add_shirt, name='add_shirt'),
    path('awards/', views.AwardList.as_view(), name= "awards_index"),
    path('awards/<int:pk>/', views.AwardDetail.as_view(), name = 'award_detail'),
    path('awards/create/', views.AwardCreate.as_view(), name = 'awards_create'),
    path('awards/<int:pk>/update/', views.AwardUpdate.as_view(), name= 'award_update'),
    path('awards/<int:pk>/delete/', views.AwardDelete.as_view(), name = 'award_delete'),
    path('bands/<int:band_id>/assoc_award/<int:award_id>/', views.assoc_award, name = 'assoc_award'),
]
