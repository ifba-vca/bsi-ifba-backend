from rest_framework import (generics, filters)
from teachers.models import (Teacher, Skill)
from teachers.serializers import (TeacherSerializer, SkillSerializer)
from drf_yasg.utils import swagger_auto_schema


class SkillsViewSet(generics.ListAPIView):
    queryset = Skill.objects.all().order_by('name')
    serializer_class = SkillSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']


class TeachersViewSet(generics.ListAPIView):
    queryset = Teacher.objects.all().order_by('name')
    serializer_class = TeacherSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'skills__name']
