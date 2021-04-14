from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('sightings/', views.sightings, name = "sightings"),
    # path('sightings/<unique_squirrel_id>/', views.update_sighting, name = "update"),
    path('sightings/add/', views.create_sighting, name = "add"),
    path('sightings/stats/', views.stats, name = "stats"),
    path('sightings/<unique_squirrel_id>/', views.update_sighting, name = "update"),
]
