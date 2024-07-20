from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Tweet(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author.username
