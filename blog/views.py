from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework import permissions

from blog.serializers import CategorySerializer, TagSerializer, PostSerializer
from blog.models import Category, Post, Tag

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('name')
    serializer_class = TagSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer

