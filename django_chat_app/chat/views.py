from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Chat, Message, ChatMessage
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



# Chat with bot
@login_required
def chat_view(request):
    if request.method == 'POST':
        message = request.POST['message']
        ChatMessage.objects.create(sender=request.user, content=message)
        #TODO: Generate chat bot response and save
        # Bot response
        bot_response = generate_response(message)
        # Save the message even for the bot
        bot_message = ChatMessage.objects.create(content=bot_response, sender=None)
    messages = ChatMessage.objects.order_by('timestamp')[:50]
    context = {'messages': messages}
    return render(request, 'chatbot/chat.html', context)

# Generate responses
def generate_response(message):
    keywords = ['hi', 'hello', 'hi']
    # Check if the messsage has any of the keyword
    if message.lower() in keywords:
        return "Hello human"
    else:
        return "Sorry, I can only understand and respond to greetings now"




# @login_required
# # Chat with someone
# # def chat_view(request, chat_id):
# #     chat = get_object_or_404(Chat, id=chat_id, users=request.user)
# #     messages = Message.objects.filter(chat=chat).order_by('timestamp')
# #     if request.method == 'POST':
# #         form = MessageForm(request.POST)
# #         if form.is_valid():
# #             message = form.save(commit=False)
# #             message.chat = chat
# #             message.sender = request.user
# #             message.save()
# #             return redirect('chat_view', chat_id=chat.id)
# #     else:
# #         form = MessageForm()
# #     context = {'chat': chat, 'messages': messages, 'form': form}
# #     return render(request, 'chat/chat_view.html', context)


# Sending the message
@login_required
def send_message(request, chat_id):
    chat = Chat.objects.get(id=chat_id)

    if request.method == 'POST':
        message_content = request.POST['message']
        sender = request.user
        message = Message.objects.create(chat=chat, content=message_content, sender=sender)

        # Redirect to chat view after sending
        return redirect('chat_view', chat_id=chat.id)

    else:
        # If the request method is not POST, display an error message
        messages.error(request, 'Invalid request method.')
        # return redirect('chat_list')
        return redirect('chat_view')
