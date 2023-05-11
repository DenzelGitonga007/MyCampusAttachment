from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Message, Chat

# Create your views here.
@login_required
def chat_view(request, user_id):
    user = User.objects.get(id=user_id)
    chat, created = Chat.objects.get_or_create(users__in=[request.user, user])
    messages = chat.messages.order_by('-timestamp').all()[:50]
    context = {
        'user': user,
        'messages': messages[::-1],
        'chat_id': chat.id
    }
    return render(request, 'chat.html', context)

# Sending the message
@login_required
def send_message(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        chat_id = request.POST.get('chat_id')
        chat = Chat.objects.get(id=chat_id)
        message = Message(text=text, user=request.user)
        chat.messages.add(message)
        message.save()
        return redirect('chat_view', user_id=chat.users.exclude(id=request.user.id).first().id)

def get_messages(request, chat_id, timestamp):
    chat = Chat.objects.get(id=chat_id)
    messages = chat.messages.filter(timestamp__gt=timestamp).order_by('-timestamp')
    return JsonResponse({
        'messages': [{
            'text': message.text, 
            'user': message.user.username, 
            'timestamp': message.timestamp.isoformat()} for message in messages]})
