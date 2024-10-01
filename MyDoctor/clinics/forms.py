from django import forms
from .models import Clinic, Expertise

class ClinicRegistrationForm(forms.ModelForm):
    expertise = forms.ModelMultipleChoiceField(queryset=Expertise.objects.all(), widget=forms.CheckboxSelectMultiple)
    city = forms.ChoiceField(choices=[('city1', 'City 1'), ('city2', 'City 2')])

    class Meta:
        model = Clinic
        fields = ['name', 'city', 'expertise', 'address', 'description']
