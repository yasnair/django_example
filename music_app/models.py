
#from pyexpat import model
from operator import index
import uuid
from django.db import models
from django.forms import model_to_dict


# Create your models here.

class User(models.Model):
    id           = models.CharField(primary_key=True, max_length=255, editable=True)
    display_name = models.CharField(max_length=255)
    #email        = models.EmailField(max_length=255)
    create_at    = models.DateTimeField(auto_now_add=True)
    last_update  = models.DateTimeField(auto_now=True)
    playlists    = models.ManyToManyField('Playlist', through='Users_Playlists', blank=True)

    class Meta:
        ordering = ['display_name']
        indexes  = [
            models.Index(fields=['display_name'])
        ]

class Playlist(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name          = models.CharField(max_length=255)
    collaborative = models.BooleanField(null=False, default=False) 
    public        = models.BooleanField(null=False, default=False)
    description   = models.CharField(max_length=255, null=True)
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['name']
        indexes  = [
            models.Index(fields=['name'])
        ]

    

    
class Users_Playlists(models.Model):
    USER_TYPE_OWNER = 'O'
    USER_TYPE_COLLA = 'C'
    USER_TYPE_CHOICES = [
        (USER_TYPE_OWNER, 'Owner'),
        (USER_TYPE_COLLA, 'Collaborator')

    ]
    user      = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist  = models.ForeignKey(Playlist, on_delete=models.CASCADE)
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
