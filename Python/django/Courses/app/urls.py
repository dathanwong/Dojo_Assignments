from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home),
    path("course/create/", views.create),
    path("course/destroy/<int:id>", views.destroy),
    path("course/<int:id>/delete", views.delete)
]
