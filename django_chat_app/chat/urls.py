from django.urls import path
from . import views

urlpatterns = [
    path('create_chart/', views.create_chat, name='create_chat'), # create a chat
    # path('chat/<int:chat_id>/', views.chat_view, name='chat_view'), # launch chat
    path('chat/', views.chat_view, name='chat'), # chat with bot
    path('chat/<int:chat_id>/send-message/', views.send_message, name='send_message'),
]