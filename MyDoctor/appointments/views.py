from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from MyDoctor.clinics.models import Clinic
from .models import Appointment

def book_appointment(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    available_appointments = Appointment.objects.filter(clinic=clinic, is_booked=False)
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.patient = request.user
        appointment.is_booked = True
        appointment.save()
        return redirect('confirmation')  # Redirect to a confirmation page
    return render(request, 'appointments/book.html', {'clinic': clinic, 'available_appointments': available_appointments})
