from cgitb import lookup
from re import I
from django.shortcuts import get_object_or_404, render
from music_app.models import User, Playlist

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, PlaylistSerializer, ArtistSerializer, AlbumSerializer, TrackSerializer
from .models import Album, Artist, User, Track



#User 
class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(active=True)
    serializer_class = UserSerializer
    

    def get_serializer_context(self):
        return {'request': self.request}    



#Playlist
class PlaylistViewSet(ModelViewSet):
    serializer_class = PlaylistSerializer

    def get_queryset(self):
        return Playlist.objects.filter(users__id = self.kwargs['user_pk']).filter(active=True)

    
    def get_serializer_context(self):
        return {'users_id': self.kwargs['user_pk']}

#Artist
class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.filter(active=True)
    serializer_class = ArtistSerializer
    
    def get_serializer_context(self):
        return {'request': self.request} 


#Album
class AlbumViewSet(ModelViewSet):
    serializer_class = AlbumSerializer
    
    def get_queryset(self):
        return Album.objects.filter(artist__id = self.kwargs['artist_pk']).filter(active=True)

    
    def get_serializer_context(self):
        return {
            'artist_id': self.kwargs['artist_pk'],
            'album_id': self.kwargs['pk'],
        }  

#Track
class TrackViewSet(ModelViewSet):
    serializer_class = TrackSerializer

    def get_queryset(self):
        return Track.objects.filter(artist__id = self.kwargs['artist_pk']).filter(active=True)







        
        









                   