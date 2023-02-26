# blog/models.py
from django.db import models
from django.urls import reverse

class Post(models.Model):
    name = models.TextField()

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])