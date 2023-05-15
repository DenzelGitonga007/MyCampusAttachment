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
    user = request.user
    chat, created = Chat.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_message = request.POST.get('text')
        bot_response = get_bot_response(user_message)

        message = Message.objects.create(user=user, text=user_message)
        bot_message = Message.objects.create(user=None, text=bot_response)

        return JsonResponse({'response': bot_response})

    else:
        messages = Message.objects.filter(user=user) | Message.objects.filter(user=None)
        context = {'messages': messages}
        return render(request, 'chat/chat_view.html', context)




