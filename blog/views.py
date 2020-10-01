from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import (viewsets, permissions, generics, filters)

from blog.serializers import CategorySerializer, TagSerializer, PostSerializer
from blog.models import Category, Post, Tag

class CategoriesViewSet(generics.ListAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']

class TagsViewSet(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all().order_by('name')
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']

class PostsViewSet(generics.ListAPIView):
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']

