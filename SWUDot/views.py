from .models import User
from .models import StoreInfo
from .models import Review

from rest_framework import generics
from django.views.generic.list import ListView
from .serializers import *

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class UserListAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )

class UserDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)

class StoreInfoListAPI(generics.ListCreateAPIView):
    queryset = StoreInfo.objects.all()
    serializer_class = StoreInfoSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )

class StoreInfoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = StoreInfo.objects.all()
    serializer_class = StoreInfoSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class ReviewListAPI(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )

class ReviewDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class SchoolInfoListAPI(generics.ListCreateAPIView):
    queryset = SchoolAdressBook.objects.all()
    serializer_class = SchoolInfoSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class SchoolInfoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolAdressBook.objects.all()
    serializer_class = SchoolInfoSerializer
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


