from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.wall),
    path('logout', views.logout),
    path('message/create', views.createMessage),
    path('comment/create', views.createComment),
    path('message/<int:messageID>/delete', views.deleteMessage)
]
