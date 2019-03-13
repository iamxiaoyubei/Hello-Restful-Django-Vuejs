from django.db import models

# Create your models here.
class WebsiteUser(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.TextField()
    avatar = models.URLField()