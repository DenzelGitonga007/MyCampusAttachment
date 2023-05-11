from django.urls import path
from . import views

urlpatterns = [
    path('create_chart/', views.create_chat, name='create_chat'), # create a chat
    path('chat/<int:pk>/', views.chat_view, name='chat_view'),
]