from django.contrib import admin

# Register your models here.
from .models import Chat, Message


def username(obj):
    return obj.user.username


# # Chat
# class ChatAdmin(admin.ModelAdmin):
#     list_display = (username,)

# Messages
class MessageAdmin(admin.ModelAdmin):
    list_display = (username, 'timestamp', 'text')


admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)

