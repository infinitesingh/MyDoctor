from django.db import models
from clinics.models import Clinic
from users.models import User
# Create your models here.
class Appointment(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)
