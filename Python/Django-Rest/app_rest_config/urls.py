
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, MusicViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'musics', MusicViewSet)
router.register(r'Users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


