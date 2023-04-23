from rest_framework import serializers
from api.models import Users, Institutions

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('_id','UserId', 'Email', 'Password', 'Number')

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institutions
        fields=('_id', 'Name', 'Address', 'PhoneNumber')