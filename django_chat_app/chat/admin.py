from django.contrib import admin

# Register your models here.
from .models import ChatMessage

class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'content')
admin.site.register(ChatMessage)