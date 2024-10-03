from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id','title','author','body','date_added']


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id','username',)