from rest_framework import serializers
from .models import Course

#class CourseSerializer(serializers.ModelSerializer):
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Course 
        fields = ('id', 'url', 'name', 'language', 'price')

## HyperlinkedSerializer put hyperlinks, i.e. urls for accessing each object