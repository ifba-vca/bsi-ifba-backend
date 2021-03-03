from django.test import TestCase
from teachers.models import Teacher, Skill


class TeachersTestCase(TestCase):
    def setUp(self) -> None:
        skill = Skill.objects.create(name='Skill 1')
        skill2 = Skill.objects.create(name='Skill 2')
        teacher = Teacher.objects.create(
            name='Teacher 1',
            title='Backend developer',
            description='New teste',
        )

        teacher.skills.set([skill, skill2])

    def test_get_teacher_1(self):
        teacher = Teacher.objects.first()
        first_skill = teacher.skills.first()
        count_skills = teacher.skills.count()

        self.assertEquals(teacher.name, 'Teacher 1')
        self.assertEquals(first_skill.name, 'Skill 1')
        self.assertEquals(count_skills, 2)
