from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('addBook', views.addBook),
    path('book/<int:id>', views.book),
    path('addAuthor', views.addAuthor),
    path('authors', views.authors),
    path('addNewAuthor', views.addNewAuthor),
    path('authors/<int:id>', views.author),
    path('addBookAuthor', views.addBookAuthor)
]
