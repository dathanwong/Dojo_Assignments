from django.urls import path
from . import views

urlpatterns = [
    path('', views.random, name='home'),
    path('/reset', views.reset, name='reset'),
    path('/submit', views.submit, name='submit')
]
