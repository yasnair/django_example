from django.urls import path
from . import views

#URLConf
urlpatterns = [
    #path('users/', UserView.as_view()), 
    path('users/', views.user_list),
    path('users/<id>/', views.user_detail), 
]
