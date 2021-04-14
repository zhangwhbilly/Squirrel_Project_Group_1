from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "home"),
    path('sightings/sightings', views.sightings, name = "sightings"),
    path('sightings/<unique_squirrel_id>', views.update, name = "update"),
    path('sightings/add/', views.add, name = "add"),
    path('sightings/stats', views.stats, name = "stats"),
]
