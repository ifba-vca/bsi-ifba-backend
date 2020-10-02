from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Category, Post, Tag


class PostTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='TestCaseCategory')

        user = User.objects.create(
            is_superuser=False,
            username='user_test',
            email='user_test@test.com',
            password='123456',
            first_name='test',
            last_name='user'
        )

        tag = Tag.objects.create(name='TestCaseTag')

        post = Post.objects.create(
            title='TestCasePost',
            description='Description Test',
            author=user,
            category=category,
        )

        post.tags.set([tag])

    def test_get_category(self):
        category = Category.objects.get(name='TestCaseCategory')
        self.assertEquals(category.__str__(), 'TestCaseCategory')

    def test_get_author(self):
        author = User.objects.get(email='user_test@test.com')
        self.assertEquals(author.email, 'user_test@test.com')

    def test_get_post(self):
        post = Post.objects.get(title='TestCasePost')
        self.assertEquals(post.__str__(), 'TestCasePost')

    def test_get_tag(self):
        tag = Tag.objects.get(name='TestCaseTag')
        self.assertEquals(tag.__str__(), 'TestCaseTag')
