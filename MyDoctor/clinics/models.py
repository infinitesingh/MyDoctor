from django.db import models
from users.models import User


class Clinic(models.Model):
    CLINIC_EXPERTISE_CHOICES = [
        ('childcare', 'Childcare'),
        ('ent', 'ENT'),
        ('gastro', 'Gastro'),
        ('general', 'General Medicine'),
        # Add more expertise options as required
    ]

    manager = models.OneToOneField(User, on_delete=models.CASCADE, related_name='clinic')
    name = models.CharField(max_length=255)
    registrationNo = models.CharField(max_length=100) 
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)  # Now, it will be filled automatically based on the zipcode
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    expertise = models.CharField(max_length=50, choices=CLINIC_EXPERTISE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    
    # Location fields
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    
    # For calculating distance from the patient's location
    reviews = models.IntegerField(default=0)
    review_score = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def get_lat_lng(self):
        return (self.latitude, self.longitude)

    class Meta:
        ordering = ['-review_score', '-reviews']
