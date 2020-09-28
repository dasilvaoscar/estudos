from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_rest_config.views import UserViewSet


urlpatterns = [

    path('', include('app_rest_config.urls')),
    path('admin/', admin.site.urls),

]


