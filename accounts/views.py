from django.shortcuts import render

# Create your views here.
from django import forms
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework.generics import *
# 회원가입 페이지
class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name','email']

    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('비밀번호 오류')

        return cd['password2']


class UserListAPI(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserCreateAPI(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserCreateSerializer

class UserDeleteAPI(DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserDeleteSerializer

class UserUpdateAPI(UpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserUpdateSerializer