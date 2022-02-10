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
from .serializers import UserSerializer, PlaylistSerializer
from .models import User



#User 
class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(active=True)
    serializer_class = UserSerializer
    lookup_field = 'user_id'

    def get_serializer_context(self):
        return {'request': self.request}

    @action(detail=True)
    def get_playlists(self,request, pk=None):
        user           = self.get_object()
        user_playlists = Playlist.objects.filter(user=user)
        serializer     = PlaylistSerializer(user_playlists, many = True)
        return Response(serializer.data)
        



#Playlist
class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    lookup_field = 'playlist_id'
    
    def get_serializer_context(self):
        return {'request': self.request}

        
        









                   