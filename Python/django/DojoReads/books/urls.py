from django.urls import path, include
from . import views

#Pattern starts with /books
urlpatterns = [
    path('', views.books),
    path('/add', views.addBooksPage),
    path('/create', views.createBook),
    path('/<int:bookID>', views.bookPage),
    path('/<int:bookID>/addReview', views.addReview),
    path('/<int:bookID>/<int:reviewID>/delete', views.deleteReview)
]
