from dataclasses import fields
from django import views
from rest_framework import serializers
from .models import User, Playlist, UsersPlaylists, Album, AlbumsArtists, Artist, Track
from django.core.exceptions import ObjectDoesNotExist

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ('id', 'display_name', 'active','create_at', 'last_update', 'playlists')
        depth  = 1

        


class PlaylistSerializer(serializers.ModelSerializer):    
    class Meta:
        model   = Playlist
        fields  = ('id', 'name', 'collaborative','public', 'description','create_at', 'last_update', 'users')
        depth  = 1
    
    def create(self, validated_data):
        user_id = self.context['users_id']
        user = User.objects.filter(id=user_id).get()
        playlist = Playlist.objects.create(**validated_data)
        UsersPlaylists.objects.create(user=user, playlist=playlist)

        return playlist 

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Artist
        fields = ('id', 'name', 'create_at', 'last_update', 'albums')
        depth  = 1
        

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Album
        fields = ('id', 'name', 'type','release_date', 'create_at', 'last_update', 'artists')
        depth  = 1
        
  


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Track
        fields = ('id', 'name','duration_ms','explicit', 'create_at', 'last_update', 'album')
        depth  = 1
        
  



