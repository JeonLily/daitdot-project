from rest_framework import serializers
from django.contrib.auth import get_user_model
from SWUDot.models import *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id','password','username','number','temp_number','user_image','email','last_name')


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username','first_name','last_name','password','email','number','temp_number', 'user_image','isStudent')

    def create(self, validated_data):
        user = get_user_model().objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()

        return user

class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()

    def delete(request, username):
        user = get_user_model()
        u = user.objects.get(username=username)
        u.delete()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username')