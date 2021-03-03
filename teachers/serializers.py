from rest_framework import serializers
from teachers.models import Skill, Teacher


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(read_only=True, many=True)

    class Meta:
        model = Teacher
        fields = '__all__'
