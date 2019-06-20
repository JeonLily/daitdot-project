from django.urls import path

from .views import *

urlpatterns = [
    path('list/',UserListAPI.as_view()),
    path('create/',UserCreateAPI.as_view()),
    path('delete/<int:pk>/',UserDeleteAPI.as_view()),
    path('update/<int:pk>/', UserUpdateAPI.as_view()),
]