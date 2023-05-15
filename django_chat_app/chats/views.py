from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Message, Chat
from django.contrib.auth.decorators import login_required



def get_bot_response(user_message):
    if user_message is None:
        return "I'm sorry, I didn't receive your message."
    
    responses = {
        'hi': 'Hello!',
        'how are you': 'I am doing well, thank you!',
        'bye': 'Goodbye!',
    }
    
    if user_message.lower() in responses:
        return responses[user_message.lower()]
    else:
        return "I'm sorry, I didn't understand your message."



@login_required
@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('text')
        bot_response = get_bot_response(user_message)
        
        # Save user message to database
        user = request.user
        chat = Chat.objects.filter(user=user).first()
        # Create a chat if none exists
        if not chat:
            chat = Chat.objects.create()
            chat.user.add(request.user)
        message = Message.objects.create(user=request.user, text=user_message)
        # Save bot response to database
        bot_message = Message.objects.create(user=None, text=bot_response)

        # Return bot response as JSON
        return JsonResponse({'response': bot_response})
        
    else:
        return render(request, 'chat/chat_view.html')



