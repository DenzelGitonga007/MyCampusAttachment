from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter message...'}))

    class Meta:
        model = Message
        fields = ['text']