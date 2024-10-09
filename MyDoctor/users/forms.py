# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    fullname = forms.CharField(max_length=255, required=True, label="Full Name")
    city = forms.ChoiceField(choices=[
        ('', 'Select your city'),
        ('New York', 'New York'),
        ('Los Angeles', 'Los Angeles'),
        ('Chicago', 'Chicago'),
        # Add more cities as required
    ], required=True, label="City")
    class Meta:
        model = User
        fields = ['fullname','username', 'email', 'password1', 'password2']
