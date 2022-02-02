
#from pyexpat import model
from operator import index
import uuid
from django.db import models


# Create your models here.
class Playlist(models.Model):
    id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name          = models.CharField(max_length=255)
    collaborative = models.BooleanField(null=False, default=False) 
    public        = models.BooleanField(null=False, default=False)
    description   = models.CharField(max_length=255)
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'music_playlists'
        indexes  = [
            models.Index(fields=['name'])
        ]

    



class User(models.Model):
    id           = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    display_name = models.CharField(max_length=255)
    uri          = models.CharField(max_length=255)
    href         = models.URLField(max_length=200)
    create_at    = models.DateTimeField(auto_now_add=True)
    last_update  = models.DateTimeField(auto_now=True)
    playlists    = models.ManyToManyField(Playlist)

    class Meta:
        db_table = 'music_users'
        indexes  = [
            models.Index(fields=['display_name'])
        ]


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
