from django.urls import path
from .views import playlist_detail
from . import views

#URLConf
urlpatterns = [
    #path('users/', UserView.as_view()), 
    path('users/', views.user_list),
    path('users/<id>/', views.user_detail),
    path('playlist/<int:pk>/', views.playlist_detail, name='playlist-list')

    
]
