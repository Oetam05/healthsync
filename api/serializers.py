from rest_framework import serializers
from api.models import *

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Doctor
        fields=('_id', 'user_id','name', 'address', 'phone_number',"email", 'password')
class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model=Patient
        fields=('_id', 'user_id','name', 'address', 'phone_number',"email", 'password')
class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Appointment
        fields=('_id', 'patient', 'doctor', 'date', 'time')
class historySerializer(serializers.ModelSerializer):

    class Meta:
        model=History
        fields=('_id', 'cita', 'description', 'rating')


