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
from .serializers import UserSerializer, PlaylistSerializer, AlbumSerializer, TrackSerializer, ArtistSerializer
from .models import Album, User



#User 
class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(active=True)
    serializer_class = UserSerializer
    

    def get_serializer_context(self):
        return {'request': self.request}    



#Playlist
class PlaylistViewSet(ModelViewSet):
    queryset  = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    #lookup_field = 'playlist_id'

    def get_queryset(self):
        return Playlist.objects.filter(users__id = self.kwargs['user_pk'])

    
    def get_serializer_context(self):
        return {'users_id': self.kwargs['user_pk']}


#Album
class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
    def get_serializer_context(self):
        return {'request': self.request}    

#Artist
class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    
    def get_serializer_context(self):
        return {'request': self.request} 

   

        
        









                   