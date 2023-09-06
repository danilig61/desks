from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Advertisement, Response, User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ('category', 'title', 'text')

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('text',)