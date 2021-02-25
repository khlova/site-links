from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    long_link = forms.CharField(
        label='Длинная ссылка',
        required=True,
        max_length = 250,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ссылку'})
    )
    short_link = forms.CharField(
        label='Сокращенная ссылка',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите слово сокращение'})
    )
    class Meta:
        model = Link
        fields = ['long_link', 'short_link', 'user']
        widgets = {'user': forms.HiddenInput()}
