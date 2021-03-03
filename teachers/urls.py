from django.urls import path
from . import views

urlpatterns = [
    path('', views.TeachersViewSet.as_view(), name='teachers'),
    path('skills', views.SkillsViewSet.as_view(), name='skills'),
]

