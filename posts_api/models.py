from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=255)

class Post(models.Model):
    user_id = models.IntegerField(null=True)
    username = models.CharField(max_length=32, null=True)
    title = models.CharField(max_length=255)
    formBody = models.TextField(null=True, blank=True)
    imageURL = models.CharField(max_length=200, null=True, blank=True)
    likes = models.IntegerField(null=True)
    upvoted = ArrayField(models.IntegerField(), null=True)
    downvoted = ArrayField(models.IntegerField(), null=True)
    created = models.DateTimeField(auto_now_add=True)