from django.db import models
from django.contrib.auth.models import User
# Import the settings
from django.conf import settings

# Create your models here.
# Chat and message models

class Message(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Chat(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chats')
    messages = models.ManyToManyField(Message)