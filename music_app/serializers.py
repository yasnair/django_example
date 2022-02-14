from dataclasses import fields
from django import views
from rest_framework import serializers
from .models import User, Playlist, UsersPlaylists

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ('id', 'display_name', 'active','create_at', 'last_update')
        


class PlaylistSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(active=True)
    )

    class Meta:
        model   = Playlist
        fields  = ('id', 'name', 'collaborative','public', 'description', 'create_at', 'last_update', 'owner')
        read_only_fields = ['owner']

    '''
    def create(self, validated_data):
        playlist = Playlist(**validated_data)
        playlist.save()
        UsersPlaylists.objects.create(user=self.owner, playlist = playlist)

        return playlist
    '''
  



