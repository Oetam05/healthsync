from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    username=serializers.CharField()
    password=serializers.CharField()

    class Meta:
        model=User
        fields=('id','username', 'password')

    def create(self, validate_data):
        instance=User()
        instance.username=validate_data.get('username')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance
    
    def validate_username(self, data):
        users=User.objects.filter(username=data)
        if len(users)!=0:
            raise serializers.ValidationError("Ya existe este nombre de usuario")
        else:
            return data

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Doctor
        fields=('_id', 'user', 'id_number','name', 'address', 'phone_number',"email")

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model=Patient
        fields=('_id', 'user', 'id_number','name', 'address', 'phone_number',"email")

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Appointment
        fields=('_id', "patient", "doctor", 'date', 'time')

class historySerializer(serializers.ModelSerializer):

    class Meta:
        model=History
        fields=('_id', 'appointment', 'description', 'rating')


