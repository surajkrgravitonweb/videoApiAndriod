# yourapp/models.py
from django.db import models

class Project1(models.Model):
    video_upload = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=255)
    description = models.TextField()

class Project2(models.Model):
    video_upload = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnails = models.ImageField(upload_to='thumbnails/')
    link = models.URLField()

