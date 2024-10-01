from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('clinic_admin', 'Clinic Admin'),
    )
    
    role = forms.ChoiceField(choices=ROLE_CHOICES)
    city = forms.ChoiceField(choices=[('city1', 'City 1'), ('city2', 'City 2')])

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('role', 'city')
