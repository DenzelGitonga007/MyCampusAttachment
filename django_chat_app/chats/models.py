from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
# Chats
class Chat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chats')

    def __str__(self):
        return self.user.username

class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages', null=True)
    # chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages') 
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return "{}".format(self.text)
