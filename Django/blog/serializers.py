from rest_framework import serializers
from blog.models import EndPoints

class EndPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPoints
        exclude = ('id',)