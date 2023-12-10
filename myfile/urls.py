# yourapp/urls.py
from django.urls import path
from .views import Project1ListCreateView, Project2ListCreateView

urlpatterns = [
    path('project1/', Project1ListCreateView.as_view(), name='project1-list-create'),
    path('project2/', Project2ListCreateView.as_view(), name='project2-list-create'),
]
