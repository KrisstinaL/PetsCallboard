from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class ProfileSer(serializers.ModelSerializer):
    user = UserSer()

    class Meta:
        model = Profile
        fields = ("user", "avatar", "phone", "first_name", "last_name")


class ProfileUpdateSer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar", "phone", "first_name", "last_name")


class AvatarUpdateSer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar",)