from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model

# Create a new chat
class UserChoiceForm(forms.Form):
    user = forms.MultipleChoiceField(
        queryset=get_user_model().objects.exclude(id=self.request.user.id),
        label = 'Select a user',
        widget = forms.Select(attrs={'class': 'form-control'}),
    )