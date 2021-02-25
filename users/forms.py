from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

    email = forms.EmailField(
        label='Введите E-mail',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email',  'password1']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Введите E-mail',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите E-mail'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


