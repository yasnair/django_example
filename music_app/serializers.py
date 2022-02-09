from dataclasses import fields
from django import views
from rest_framework import serializers
from .models import User, Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Playlist
        fields  = ('id', 'name', 'collaborative','public', 'description', 'create_at', 'last_update')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ('id', 'display_name', 'create_at', 'last_update')
        



