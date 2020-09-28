from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Music

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class MusicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'