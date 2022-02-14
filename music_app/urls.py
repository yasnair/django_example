import imp
from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
import pprint



router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'playlist', views.PlaylistViewSet)
router.urls



#URLConf
urlpatterns = router.urls
#
#urlpatterns = [
#   path('', include(router.urls)),
#]




