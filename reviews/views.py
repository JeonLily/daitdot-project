from django.shortcuts import render

# Create your views here.
from django import forms
from .serializers import *
from rest_framework.generics import *
from SWUDot.models import *
from SWUDot.serializers import ReviewSerializer
from .models import *
# 회원가입 페이지
class ReiviewForm(forms.ModelForm):
    review_image = forms.ImageField(label='reviewImage', widget=forms.URLInput)
    review_score = forms.FloatField(label='reviewScore', widget=forms.TextInput)
    text = forms.CharField(label='reviewText', widget=forms.TextInput, max_length=300)
    user_name = forms.CharField(label='userName', widget= forms.TextInput)
    store = forms.CharField(label='store', widget=forms.TextInput)

    class Meta:
        model = Review
        fields = ['user_name', 'review_score', 'store','text', 'review_image']

class ReviewListAPI(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateAPI(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer