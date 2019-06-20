
from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreInfo
        fields = ('id', 'st_name')


class StoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreInfo
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    user_name = UserInfoSerializer(read_only=True)
    store = StoreSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'


class SchoolInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolAdressBook
        fields = ('id', 'name')


class SchoolInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolAdressBook
        fields = '__all__'