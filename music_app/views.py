from django.shortcuts import render
from django.http import HttpResponse
from music_app.models import User, Playlist


# Create your views here.
   
def main(request):
    return HttpResponse('Hello Word')
                   