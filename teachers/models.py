from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField()
    skills = models.ManyToManyField(Skill)
    photo = models.ImageField(upload_to='teachers_photo')

    def __str__(self):
        return self.name
