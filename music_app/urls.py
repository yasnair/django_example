
from cgitb import lookup
from django.urls import path, include
from rest_framework_nested import routers
from . import views
from pprint import pprint



router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('artists', views.ArtistViewSet)
router.register('albums', views.AlbumViewSet, basename='Album')

users_router=routers.NestedDefaultRouter(router, 'users', lookup='user')
users_router.register('playlists', views.PlaylistViewSet, basename='user-playlists')
artists_router=routers.NestedDefaultRouter(router, 'artists', lookup='artist')
artists_router.register('albums', views.AlbumViewSet, basename='artist-album')
albums_router=routers.NestedDefaultRouter(router, 'albums', lookup='albums')
albums_router.register('tracks', views.TrackViewSet, basename='album-track')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('', include(users_router.urls)),
    path('', include(artists_router.urls)),
    path('', include(albums_router.urls)),
]





