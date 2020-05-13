from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('addDojo', views.addDojo),
    path('addNinja', views.addNinja),
    path('delete/<int:dojoId>', views.deleteDojo, name='deleteDojo')
]
