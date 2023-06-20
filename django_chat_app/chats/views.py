from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Message, Chat
from django.contrib.auth.decorators import login_required



def get_bot_response(user_message):
    if user_message is None:
        return "I'm sorry, I didn't receive your message."
    
    responses = {
        'hi': 'Hello! 👋',
        'how are you?': 'I am doing well, thank you! 🙏',
        'okay': 'Alright, I hope I was helpful, thank you.',
        'thank you': 'My pleasure 🤗',
        'bye': 'Goodbye! 👋',
        'nice to meet you': 'Nice to meet you too!',
        'what are you doing?': 'I am here to assist you and answer your questions. 🤗',
        'what about you, where are you from?': 'I am an AI bot, I do not have a physical location. 🤖',
        'ezen financials': 'Ezen Financials is an all-in-one web based Financial ERP for Microfinance, Sacco, Property Management, Property sales, Valuation, CRM, HR & Payroll and Financial Accounting that makes business life easier for Saccos, Microfinance, Property managers, landlords and any other business. 📝✍️',    
        'tell me about ezen partners': 'Since 2013 we are a Swiss Army knife when it comes to automated and efficient property management solutions that enable landlords and managers of residential and association properties to take complete control of every aspect of their business, including the rent, vacancy and maintenance cycles. It is amazingly great how Ezen streamlines management of the rent cycle with key features such as tenant and lease tracking, full general ledger accounting, automated rent and late fee reminders and on-demand reports. Additionally, rent collection can be automated and property managers can receive online payments via Ezen tenant mobile application 📝✍️.',
        'where are you located?': 'We are on 7th Floor, Twiga Towers, Muranga Road - Nairobi',
        
    }
    
    if user_message.lower() in responses:
        return responses[user_message.lower()]
    else:
        return "I'm sorry, as an AI model, I am not yet trained to interpret that. Try asking about Ezen Partners"



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




