
#from pyexpat import model
from operator import index
from tkinter import CASCADE
from django.db import models
from django.contrib import admin


# Create your models here.

class User(models.Model):
    id           = models.CharField(primary_key=True, max_length=255, editable=True)
    display_name = models.CharField(max_length=255)
    active       = models.BooleanField(default=True) 
    create_at    = models.DateTimeField(auto_now_add=True)
    last_update  = models.DateTimeField(auto_now=True)

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
    users   = models.ManyToManyField(
                'User',
                through='UsersPlaylists',
                through_fields=('playlist', 'user'),
                related_name='playlists',
            )
    class Meta:
        ordering = ['name']
        indexes  = [
            models.Index(fields=['name'])
        ]



class UsersPlaylists(models.Model):
    OWNER  = 'O'
    COLLAB = 'C'
    USER_TYPE_CHOICES = [
        (OWNER, 'Owner'),
        (COLLAB, 'Collaborator')

    ]
    user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userplaylist')
    playlist  = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='userplaylist')
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default=OWNER)



class Artist (models.Model):
    id            = models.CharField(primary_key=True, max_length=255, editable=True)
    name          = models.CharField(max_length=255)
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    

class Album(models.Model):
    ALBUM  = 'A'
    SINGLE = 'S'
    COMPIL = 'C'
    ALBUM_TYPE_CHOICES = [
        (ALBUM, 'Album'),
        (SINGLE, 'Single'),
        (COMPIL, 'Compilation')

    ]
    id            = models.CharField(primary_key=True, max_length=255, editable=True)
    name          = models.CharField(max_length=255)
    type          = models.CharField(max_length=1, choices=ALBUM_TYPE_CHOICES, null=False)
    release_date  = models.DateField()
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    artists       = models.ManyToManyField(
                    'Artist',
                    through='AlbumsArtists',
                    through_fields=('album', 'artist'),
                    related_name='artists',
                )



class AlbumsArtists(models.Model):
    album   = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='albumartist')
    artist  = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albumartist')

class Track(models.Model):
    id            = models.CharField(primary_key=True, max_length=255, editable=True)
    name          = models.CharField(max_length=255)
    duration_ms   = models.IntegerField( )
    explicit      = models.BooleanField(default=False) 
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    album         = models.ForeignKey(AlbumsArtists, on_delete=models.CASCADE, null=False)

class UsersPlaylistsInline(admin.TabularInline):
    model = UsersPlaylists
    extra = 1
class UserAdmin(admin.ModelAdmin):
    inlines = (UsersPlaylistsInline,)

class PlaylistAdmin(admin.ModelAdmin):
    inlines = (UsersPlaylistsInline,)

