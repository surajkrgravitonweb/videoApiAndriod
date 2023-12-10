# yourapp/serializers.py
from rest_framework import serializers
from .models import Project1, Project2

class Project1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project1
        fields = '__all__'

class Project2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project2
        fields = '__all__'
