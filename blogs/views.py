from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BlogSerializer, UserSerializer
from .models import Blog
from .permissions import IsAuthorOrReadOnly
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer