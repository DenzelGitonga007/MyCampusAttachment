from django import forms
from django.contrib.auth import get_user_model

# Create a new chat
class UserChoiceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['user'] = forms.ModelChoiceField(
            queryset=get_user_model().objects.exclude(id=user.id),
            label='Select a user',
            widget=forms.Select(attrs={'class': 'form-control'}),
        )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['user'].empty_label = "Select a user"
            self.fields['user'].widget.attrs.update({'class': 'form-control'})
