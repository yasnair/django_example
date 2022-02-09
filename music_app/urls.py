import imp
from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('playlist', views.PlaylistViewSet)
router.urls


#URLConf
urlpatterns = router.urls


