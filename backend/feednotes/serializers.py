from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(allow_blank=True, allow_null=True)
    first_name = serializers.CharField(allow_blank=True, allow_null=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'author', 'body', 'date')