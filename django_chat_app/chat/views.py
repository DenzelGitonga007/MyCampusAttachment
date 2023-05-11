from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from .forms import UserChoiceForm, MessageForm


# Start chat
@login_required
def create_chat(request):
    if request.method == 'POST':
        form = UserChoiceForm(request.POST, user=request.user)
        if form.is_valid():
            # Get the selected user from the form
            selected_user = form.cleaned_data['user']
            # Get the current user
            current_user = request.user
            # Create a new chat with the selected user and current user
            chat = Chat.objects.create()
            chat.users.add(current_user, selected_user)
            # Redirect to the chat view for the newly created chat
            return redirect('chat_view', chat.id)
    else:
        form = UserChoiceForm(user=request.user)
    context = {'form': form}
    return render(request, 'chat/create_chat.html', context)

# Chat view





@login_required
def chat_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id, users=request.user)
    messages = Message.objects.filter(chat=chat).order_by('timestamp')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat = chat
            message.sender = request.user
            message.save()
            return redirect('chat_view', chat_id=chat.id)
    else:
        form = MessageForm()
    context = {'chat': chat, 'messages': messages, 'form': form}
    return render(request, 'chat/chat_view.html', context)

