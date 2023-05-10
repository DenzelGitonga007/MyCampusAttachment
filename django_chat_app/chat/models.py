from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Chat and message models

class Message(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Chat(models.Model):
    users = models.ManyToManyField(User, related_name='chats')
    messages = models.ManyToManyField(Message)