from django.db import models

# Create your models here.
PATIENT_TYPE = (
    "Yatan",
    "Ayaktan",
)


class Patient(models.Model):
    id_no = models.CharField(max_length=11)
    dosya_no = models.CharField(max_length=9)
    patient_type = models.CharField(choices=PATIENT_TYPE)
