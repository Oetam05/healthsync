from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('_id','UserId', 'Email', 'Password', 'Number','Type')

"""class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institutions
        fields=('_id', 'Name', 'Address', 'PhoneNumber')"""
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctors
        fields=('_id', 'UserId','Name', 'Address', 'PhoneNumber',"Email")
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patients
        fields=('_id','UserId', 'Name', 'Address', 'PhoneNumber', "Email")
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields=('_id', 'Patient', 'Doctor', 'Date', 'Time')
class historySerializer(serializers.ModelSerializer):
    class Meta:
        model=History
        fields=('_id', 'Cita', 'Description', 'Rating')


