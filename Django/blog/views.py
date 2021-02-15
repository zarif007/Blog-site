from blog.models import Post
from rest_framework import generics
from .models import EndPoints
from .serializers import EndPointsSerializer

class ListEndPoints(generics.ListAPIView):
    queryset = EndPoints.objects.all()
    serializer_class = EndPointsSerializer