from django.urls import path, include

from . import views

urlpatterns = [
    path('tags/', views.TagsViewSet.as_view(), name='tags'),
    path('category/', views.CategoriesViewSet.as_view(), name='category'),
    path('posts/', views.PostsViewSet.as_view(), name='posts'),
]
