
#from pyexpat import model
from operator import index
from pyexpat import model
import re
from tkinter import CASCADE
from django.db import models
from django.contrib import admin


# Principal Models

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
    active        = models.BooleanField(default=True) 
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    users         = models.ManyToManyField(
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

    def __str__(self) -> str:
        return self.name


class Artist (models.Model):
    id            = models.CharField(primary_key=True, max_length=255, editable=True)
    name          = models.CharField(max_length=255)
    active        = models.BooleanField(default=True) 
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['name']
        indexes  = [
            models.Index(fields=['name'])
        ]
    

class Album(models.Model):
    ALBUM       = 'A'
    SINGLE      = 'S'
    COMPILATION = 'C'
    APPEARS_ON  = 'AO'
    ALBUM_TYPE_CHOICES = [
        (ALBUM, 'Album'),
        (SINGLE, 'Single'),
        (COMPILATION, 'Compilation'),
        (APPEARS_ON , 'Appears_on')

    ]
    id            = models.CharField(primary_key=True, max_length=255, editable=True)
    name          = models.CharField(max_length=255)
    type          = models.CharField(max_length=10, choices=ALBUM_TYPE_CHOICES, null=False)
    release_date  = models.DateField()
    active        = models.BooleanField(default=True) 
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    artist        = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    class Meta:
        ordering = ['name']
        indexes  = [
            models.Index(fields=['name'])
        ]


class Track(models.Model):
    id            = models.CharField(primary_key=True, max_length=255, editable=True)
    name          = models.CharField(max_length=255)
    duration_ms   = models.IntegerField( )
    explicit      = models.BooleanField(default=False) 
    active        = models.BooleanField(default=True) 
    create_at     = models.DateTimeField(auto_now_add=True)
    last_update   = models.DateTimeField(auto_now=True)
    album         = models.ForeignKey(Album, on_delete=models.CASCADE, null=False, related_name='tracks')
    
    artist       = models.ManyToManyField(
                            'Artist',
                            through='ArtistTrack',
                            through_fields=('track', 'artist'),
                            related_name='artists',
                        )
    
    playlists   = models.ManyToManyField(
                    'Playlist',
                    through='PlaylistTrack',
                    through_fields=('track', 'playlist'),
                    related_name='tracks',
            )
    
    users   = models.ManyToManyField(
                'User',
                through='PlaylistTrack',
                through_fields=('track', 'user'),
                related_name='tracks',
            )

    
    class Meta:
        ordering = ['name']
        indexes  = [
            models.Index(fields=['name'])
        ]
    
    def __str__(self) -> str:
        return self.name

#Through
class UsersPlaylists(models.Model):
    OWNER  = 'O'
    COLLAB = 'C'
    USER_TYPE_CHOICES = [
        (OWNER, 'Owner'),
        (COLLAB, 'Collaborator')

    ]
    user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_playlist')
    playlist  = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='user_playlist')
    user_type = models.CharField(max_length=1, choices=USER_TYPE_CHOICES, default=OWNER)


class PlaylistTrack(models.Model):
    playlist  = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='playlist_track')
    track     = models.ForeignKey(Track, on_delete=models.CASCADE, related_name='playlist_track')
    user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlist_track')
    quantity  = models.IntegerField(default=1)

class ArtistTrack(models.Model):
    track           = models.ForeignKey(Track,on_delete=models.CASCADE, related_name='artist_track')
    artist          = models.ForeignKey(Artist,on_delete=models.CASCADE, related_name='artist_track')
    artist_feat   = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="artist_feat",
    )

#Inline model
class UsersPlaylistsInline(admin.TabularInline):
    model = UsersPlaylists
    extra = 1
class UserAdmin(admin.ModelAdmin):
    inlines = (UsersPlaylistsInline,)

class PlaylistAdmin(admin.ModelAdmin):
    inlines = (UsersPlaylistsInline,)

