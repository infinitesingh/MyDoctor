from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    city = forms.ChoiceField(
        choices=[('city1', 'SLN'), ('city2', 'LKO'), ('city3', 'AYD')],
        required=True,
        widget=forms.Select(attrs={'class': 'select-group', 'placeholder': 'City'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input-group', 'placeholder': 'Email'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'city']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-group','placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'input-group', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'input-group', 'placeholder': 'Confirm password'}),
        }
