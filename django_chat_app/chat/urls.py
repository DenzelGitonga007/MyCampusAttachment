from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:user_id>/', views.chat_view, name='chat_view'),
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/<int:chat_id>/<str:timestamp>/', views.get_messages, name='get_messages'),
]
