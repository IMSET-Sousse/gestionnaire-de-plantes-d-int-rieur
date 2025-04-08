from django.urls import path
from . import views

app_name = 'plantes'
urlpatterns = [
    path('', views.list_plantes, name='list_plantes'),
    path('ajouter', views.ajouter_plante, name='ajouter_plante'),
]