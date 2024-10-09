from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import ClinicRegistrationForm

def register_clinic(request):
    if request.method == 'POST':
        form = ClinicRegistrationForm(request.POST)
        if form.is_valid():
            clinic = form.save(commit=False)
            clinic.owner = request.user  # Associate the clinic with the logged-in user
            clinic.save()
            return redirect('clinic_dashboard')  # Redirect to the clinic admin dashboard
    else:
        form = ClinicRegistrationForm()
    return render(request, 'clinics/register.html', {'form': form})

def nearbyClinics(request):
    return render(request,'nearbyclinics.html')
