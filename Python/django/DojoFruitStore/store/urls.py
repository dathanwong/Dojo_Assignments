from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.storefront),
    path('submit', views.submit),
    path('checkout', views.checkout)
]
