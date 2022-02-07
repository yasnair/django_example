from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from music_app.models import User, Playlist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import UserSerializer
from .models import User
from music_app import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT'])
def user_detail(request, id):
     user = get_object_or_404(User, pk=id)
     serializer = UserSerializer(User)
     return Response(serializer.data)

''' 
    user = get_object_or_404(User, pk=id)
    if request.method == 'GET': 
        serializer = UserSerializer(User)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''        







                   