from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.books),
    path('create/', views.createBook),
    path('<int:userID>/addFavorite/<int:bookID>/', views.addFavorite),
    path('<int:userID>/removeFavorite/<int:bookID>/', views.removeFavorite),
    path('<int:bookID>', views.bookInfo),
    path('<int:bookID>/update', views.updateBook),
    path('<int:bookID>/delete', views.deleteBook),
    path('favorites', views.favorites)
]
