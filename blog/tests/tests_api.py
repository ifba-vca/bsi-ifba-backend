import json
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Tag, Category, Post


class TagsListApiTests(APITestCase):
    def test_no_tags(self):
        response = self.client.get('/tags/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {"count": 0, "next": None, "previous": None, "results": []}
        self.assertEqual(json.loads(response.content), data)

    def test_get_tags(self):
        tag = Tag.objects.create(name='teste')
        response = self.client.get('/tags/')
        data = {"count": 1, "next": None, "previous": None,
                "results": [{"id": tag.id, "name": "teste"}]}
        self.assertEqual(json.loads(response.content), data)


class CategoryListApiTests(APITestCase):
    def test_no_categories(self):
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {"count": 0, "next": None, "previous": None, "results": []}
        self.assertEqual(json.loads(response.content), data)

    def test_get_categories(self):
        category = Category.objects.create(name='teste')
        response = self.client.get('/category/')
        data = {"count": 1, "next": None, "previous": None,
                "results": [{"id": category.id, "name": "teste"}]}
        self.assertEqual(json.loads(response.content), data)


class PostsListApiTests(APITestCase):
    def test_no_posts(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {"count": 0, "next": None, "previous": None, "results": []}
        self.assertEqual(json.loads(response.content), data)

    def test_get_posts(self):
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

        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": post.id,
                    "title": post.title,
                    "description": post.description,
                    "category": {
                        "id": category.id,
                        "name": category.name
                    },
                    "tags": [
                        {
                            "id": tag.id,
                            "name": tag.name
                        },
                    ],
                    "author": user.id,
                    "created_at": post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": post.created_at.strftime('%Y-%m-%d %H:%M:%S')
                }
            ]}

        response = self.client.get('/posts/')

        self.assertEqual(json.loads(response.content), data)
