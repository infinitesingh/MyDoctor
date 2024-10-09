from django import forms
from .models import Clinic

class ClinicRegistrationForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'registrationNo','address_line_1', 'address_line_2', 'city', 'state', 'zipcode', 'expertise', 'phone_number', 'email', 'latitude', 'longitude']

        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
