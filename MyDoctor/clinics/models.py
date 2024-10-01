from django.db import models

from users.models import User

# Create your models here.
class Clinic(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    expertise = models.CharField(max_length=255)  # Multiple expertise can be handled via ManyToMany
    address = models.CharField(max_length=255)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)  # Clinic Admin
    description = models.TextField()

class Expertise(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
