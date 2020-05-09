from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('farm', views.farm),
    path('cave', views.cave),
    path("house", views.house),
    path("casino", views.casino)
]
