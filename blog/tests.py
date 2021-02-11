from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Category, Post


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = User.objects.create_user(
            username='test-123', password='testpass'
        )
        test_post = Post.objects.create(category_id=1, title='Post', excerpt='Excerpt', 
                                        content='Content', slug='Slug', author_id=1, status='published')
        
    def test_blog_contenet(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test-123')
        self.assertEqual(title, 'Post')
        self.assertEqual(content, 'Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Post')
        self.assertEqual(str(cat), 'django')