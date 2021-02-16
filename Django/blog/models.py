from django.db import models
from django.utils import timezone
from django.conf import settings

class EndPoints(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=1000)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

 
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('publishd', 'Published'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                default=1)
    title = models.CharField(max_length=150)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()
    postobjects = PostObjects()


    class Meta:
        ordering = ('-published',)

    def __str__(self): 
        return self.title