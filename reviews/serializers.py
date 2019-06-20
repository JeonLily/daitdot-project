from rest_framework import serializers
from SWUDot.models import *


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user_name','review_image','text','review_score','store')