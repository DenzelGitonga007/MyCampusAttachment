from django.shortcuts import render, redirect
from .models import Chat, Message
from .forms import UserChoiceForm


# Start chat
def create_chat(request):
    if request.method == 'POST':
        form = UserChoiceForm(request.POST)
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
        form = UserChoiceForm()
    context = {'form': form}
    return render(request, 'create_chat.html', context)
