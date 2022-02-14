
#from pyexpat import model
from operator import index
from tkinter import CASCADE
from urllib import request
from django.db import models
from django.forms import model_to_dict


# Create your models here.

class User(models.Model):
    id           = models.CharField(primary_key=True, max_length=255, editable=True)
    display_name = models.CharField(max_length=255)
    active       = models.BooleanField(null=False, default=True) 
    create_at    = models.DateTimeField(auto_now_add=True)
    last_update  = models.DateTimeField(auto_now=True)
    playlists    = models.ManyToManyField(
                    'Playlist',
                    through='UsersPlaylists',
                    through_fields=('user', 'playlist'),
                    related_name='users',
                )

    class Meta:
        ordering = ['display_name']
        indexes  = [
            models.Index(fields=['display_name'])
        ]

    def __str__(self) -> str:
        return self.display_name



class Playlist(models.Model):
    id            = models.CharField(primary_key=True, max_length=255, editable=True)
    name          = models.CharField(max_length=255)
    collaborative = models.BooleanField(default=False) 
    public        = models.BooleanField(default=True)
    description   = models.CharField(max_length=255,blank=True, null=True)
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['name']
        indexes  = [
            models.Index(fields=['name'])
        ]

    

    
class UsersPlaylists(models.Model):
    USER_TYPE_OWNER = 'O'
    USER_TYPE_COLLA = 'C'
    USER_TYPE_CHOICES = [
        (USER_TYPE_OWNER, 'Owner'),
        (USER_TYPE_COLLA, 'Collaborator')

    ]
    user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userplaylist')
    playlist  = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='userplaylist')
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default=USER_TYPE_OWNER)





'''
class Track(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name          = models.CharField(max_length=255)
    duration_ms   = models.IntegerField( )
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)

class Album(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name          = models.CharField(max_length=255)
    release_date  = models.DateField()
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)

class Artist (models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name          = models.CharField(max_length=255)
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
'''
