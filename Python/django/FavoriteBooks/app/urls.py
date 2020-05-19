from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('user/create', views.createUser),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout)
]
