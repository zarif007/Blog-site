from blog.models import Category, Post
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class PostTests(APITestCase):

    def test_view_posts(self):

        url = reverse('blog_api:listcreate')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def create_post(self):

        self.test_category = Category.objects.create(name='django')

        self.testUser1 = User.objects.create_user(
            username='test123', password='testpass'
        )

        data = {'title':'new', 'author':1, 'excerpt':'new',
                    'content':'new'}

        url = reverse('blog_api:listcreate')

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
