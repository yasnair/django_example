
from cgitb import lookup
from django.urls import path, include
from rest_framework_nested import routers
from . import views
from pprint import pprint



router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
#router.register('playlists', views.PlaylistViewSet)
users_router=routers.NestedDefaultRouter(router, 'users', lookup='user')
users_router.register('playlists', views.PlaylistViewSet, basename='user-playlists')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('', include(users_router.urls)),
]





