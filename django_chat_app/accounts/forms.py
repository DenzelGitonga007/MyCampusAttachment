from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import User
# Authentication
from django.contrib.auth import authenticate
class UserRegistrationForm(UserCreationForm):
    # username comes by default
    email = forms.EmailField(required=True)
    full_name = forms.CharField()
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        user.phone_number = self.cleaned_data['phone_number']
        if commit:
            user.save()
        return user

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        # if username and password:
        #     user = authenticate(username=username, password=password)
        #     if not user:
        #         raise forms.ValidationError("Invalid username or password")
        # else:
        #     raise forms.ValidationError("Please enter both username and password")
        user = authenticate(username=username, password=password)
        if not user:
            self.add_error('', 'Invalid username or password')
            raise forms.ValidationError('Please check the credentials you provided')
        return cleaned_data
