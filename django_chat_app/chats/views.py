from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Message

@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        bot_response = get_bot_response(user_message)
        
        # Save user message to database
        user_id = request.user.id
        chat = Chat.objects.filter(user=user_id).first()
        message = Message.objects.create(user=request.user, chat=chat, text=user_message)
        
        # Save bot response to database
        bot_message = Message.objects.create(user=None, chat=chat, text=bot_response)
        
        # Return bot response as JSON
        return JsonResponse({'response': bot_response})
        
    else:
        return render(request, 'chat/chat_view.html')
