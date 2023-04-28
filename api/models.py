from djongo import models
import uuid 
from django.contrib.auth.models import User

class Doctor(models.Model):
    _id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)    
    email= models.EmailField(max_length=50)    

class Patient(models.Model):
    _id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)    
    email= models.EmailField(max_length=50)
   
class Appointment(models.Model):
    _id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(max_length=10)
    time = models.TimeField(max_length=10)
    
class History(models.Model):
    _id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    appointment=models.OneToOneField(Appointment, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
