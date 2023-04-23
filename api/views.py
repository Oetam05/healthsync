from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from api.models import *
from api.serializers import *
# Create your views here.

def CRUD(request, id,ob):
    if request.method == 'GET':
        if ob== 'Doctor':
            users=Doctor.objects.all()
        elif ob=='Paciente':
            users=Patient.objects.all()
        elif ob=='Cita':
            users=Appointment.objects.all()
        try:
            data= JSONParser().parse(request)
        except:
            data = {}
        try:
            if data:
                if ob== 'Doctor':
                    users=Doctor.objects.filter(user_id=data['user_id'])
                elif ob=='Paciente':
                    users=Patient.objects.filter(user_id=data['user_id'])
                elif ob=='Cita':
                    users=Appointment.objects.filter(_id=data['_id'])
        except:
            data = {}
        if ob== 'Doctor':
            users_serializer = DoctorSerializer(users, many=True)
        elif ob=='Paciente':
            users_serializer = PatientSerializer(users, many=True)
        elif ob=='Cita':
            users_serializer = AppointmentSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        if ob== 'Doctor':
            users_serializer = DoctorSerializer(data=user_data)
        elif ob=='Paciente':
            users_serializer = PatientSerializer(data=user_data)
        elif ob=='Cita':
            users_serializer = AppointmentSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Registrado exitosamente", safe=False)
        return JsonResponse(users_serializer.errors, safe=False)

@csrf_exempt
def doctorApi(request, id=0):
    return CRUD(request,id,"Doctor")
@csrf_exempt
def patientApi(request, id=0):
    return CRUD(request,id,"Paciente")
@csrf_exempt
def AppointmentApi(request, id=0):
    return CRUD(request,id,"Cita")
        
@csrf_exempt
def medicalApi(request):
    if request.method=="GET":
        medical = History.objects.all()
        data= JSONParser().parse(request)
        if data['_id']:
            medical = History.objects.filter(_id=data['_id'])
        History_serializer = historySerializer(medical, many=True)
        return JsonResponse(History_serializer.data, safe=False)