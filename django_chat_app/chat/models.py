from django.db import models
from django.contrib.auth.models import User
# Import the settings
from django.conf import settings

# Create your models here.
# Chat and message models
from django.contrib.auth import get_user_model

class Chat(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chats')
    # messages = models.ManyToManyField(Message)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages', null=True)
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# Model to save chats
class ChatMessage(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.sender, self.content)