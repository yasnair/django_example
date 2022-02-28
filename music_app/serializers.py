from dataclasses import fields
from django import views
from rest_framework import serializers
from .models import ArtistTrack, User, Playlist, UsersPlaylists, Album, Artist, Track
from django.core.exceptions import ObjectDoesNotExist

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ('id', 'display_name', 'active','create_at', 'last_update', 'playlists')
        depth  = 1

        


class PlaylistSerializer(serializers.ModelSerializer):    
    class Meta:
        model   = Playlist
        fields  = ('id', 'name', 'collaborative','public', 'description', 'active','create_at', 'last_update', 'users')
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
        fields = ('id', 'name', 'active', 'create_at', 'last_update')
        depth  = 1


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Album
        release_date = serializers.DateField(input_formats=['%d-%m-%Y',])
        fields = ('id', 'name', 'type','release_date', 'create_at', 'last_update', 'artist', 'tracks')
        
        depth  = 1

    def create(self, validated_data):
        artist_id = self.context['artist_id']
        artist    = Artist.objects.filter(id=artist_id).get()
        album     = Album.objects.create(**validated_data, artist=artist)
        return album
        
  


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Track
        fields = ('id', 'name','duration_ms','explicit', 'active', 'create_at', 'last_update', 'album', 'artists')
        depth  = 1

    def create(self, validated_data):
        artist_id = self.context['artist_id']
        album_id  = self.context['album_id']
        artist    = Artist.objects.filter(id=artist_id).get()
        album     = Album.objects.filter(id=album_id).get()
        track     = Track.objects.create(**validated_data, album=album)
        ArtistTrack.objects.create(track=track, artist=artist)
        return track

    

    
    

        




