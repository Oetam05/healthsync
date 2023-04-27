from djongo import models
import uuid 
from django.contrib.auth.models import User

class Doctor(models.Model):
    _id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user_id')
    id_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)    
    email= models.EmailField(max_length=50)    

class Patient(models.Model):
    _id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user_id')
    id_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)    
    email= models.EmailField(max_length=50)
   
class Appointment(models.Model):
    _id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='user_id', db_column='patient_id')
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, to_field='user_id', db_column='doctor_id')
    date = models.DateField(max_length=10)
    time = models.TimeField(max_length=10)
    
class History(models.Model):
    _id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    cita_id=models.OneToOneField(Appointment, on_delete=models.CASCADE, db_column='cita_id')
    description = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
