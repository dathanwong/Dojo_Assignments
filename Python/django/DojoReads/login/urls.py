from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginPage),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout)
]
