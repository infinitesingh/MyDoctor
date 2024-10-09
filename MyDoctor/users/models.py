from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    fullname = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=100, blank=False)

