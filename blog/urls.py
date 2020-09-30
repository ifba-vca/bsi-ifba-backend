from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoriesViewSet)
router.register(r'tags', views.TagsViewSet)
router.register(r'posts', views.PostsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]