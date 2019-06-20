from django.urls import path

from .views import *
urlpatterns = [
    path('list/',ReviewListAPI.as_view()),
    path('create/',ReviewCreateAPI.as_view()),
]