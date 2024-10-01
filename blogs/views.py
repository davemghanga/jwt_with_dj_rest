from django.shortcuts import render
from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog
from .permissions import IsAuthorOrReadOnly
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BlogList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,IsAuthenticated,)
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
