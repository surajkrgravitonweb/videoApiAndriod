# yourapp/views.py
from rest_framework import generics
from .models import Project1, Project2
from .serializers import Project1Serializer, Project2Serializer

class Project1ListCreateView(generics.ListCreateAPIView):
    queryset = Project1.objects.all()
    serializer_class = Project1Serializer

class Project2ListCreateView(generics.ListCreateAPIView):
    queryset = Project2.objects.all()
    serializer_class = Project2Serializer
