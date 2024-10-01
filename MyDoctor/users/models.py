from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_ROLES = (
        ('patient', 'Patient'),
        ('clinic_admin', 'Clinic Admin'),
    )
    role = models.CharField(max_length=12, choices=USER_ROLES, default='patient')
    city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.username