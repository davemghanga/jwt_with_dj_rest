from django.shortcuts import render
from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class BlogList(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
