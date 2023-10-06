from django.contrib.auth.models import User
from rest_framework import serializers

from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'groups']
