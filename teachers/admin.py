from django.contrib import admin
from teachers.models import Skill, Teacher


class SkillAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    pass


admin.site.register(Skill, SkillAdmin)
admin.site.register(Teacher, TeacherAdmin)
