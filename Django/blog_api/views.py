from blog.models import Post
from rest_framework import generics
from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        DjangoModelPermissions, IsAdminUser)

from .serializers import PostSerializer
from .permissions import PostUserWritePermission

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes =[PostUserWritePermission, ]
    queryset = Post.objects.all() 
    serializer_class = PostSerializer  