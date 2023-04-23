from djongo import models


class Users(models.Model):
    TYPE_CHOICES = [    ('d', 'Doctor'),    ('p', 'Paciente'),]
    _id = models.ObjectIdField()
    UserId = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    Number = models.CharField(max_length=10)
    Type = models.CharField(max_length=1, choices=TYPE_CHOICES)  

class Doctors(models.Model):
    _id = models.ObjectIdField()
    UserId = models.CharField(max_length=15)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=10)
    #Institutions = models.ManyToManyField('Institutions')
    Email= models.EmailField(max_length=50)
class Patients(models.Model):
    _id = models.ObjectIdField()
    UserId = models.CharField(max_length=15)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=10)
    Email= models.EmailField(max_length=50)
"""class Institutions(models.Model):
    _id = models.ObjectIdField()
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=10)"""
   
class Appointment(models.Model):
    _id = models.ObjectIdField()
    Patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    Date = models.DateField(max_length=10)
    Time = models.TimeField(max_length=10)
    

class History(models.Model):
    _id = models.ObjectIdField()
    cita=models.OneToOneField(Appointment, on_delete=models.CASCADE)
    Description = models.CharField(max_length=100)
    Rating = models.CharField(max_length=100)
