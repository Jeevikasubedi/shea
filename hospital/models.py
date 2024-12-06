# models.py (hospital app)
from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AmbulanceRequest(models.Model):
    hospital = models.ForeignKey(
        'hospital.Hospital',  # This is the correct reference
        on_delete=models.CASCADE
    )
    patient_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='pending')
    # Add other fields if necessary
