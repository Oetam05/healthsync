from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.core.serializers import serialize
from django.forms.models import model_to_dict

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
                    users=Doctor.objects.filter(id_number=data['id_number'])
                elif ob=='Paciente':
                    users=Patient.objects.filter(id_number=data['id_number'])
                elif ob=='Cita':
                    users=Appointment.objects.filter(_id=data['_id'])
        except:
            data = {}
        if ob== 'Doctor':
            ob_serializer = DoctorSerializer(users, many=True)
            print(users)
            print(ob_serializer)
        elif ob=='Paciente':
            ob_serializer = PatientSerializer(users, many=True)
        elif ob=='Cita':            
            ob_serializer = AppointmentSerializer(users, many=True)
            print(ob_serializer)
            print(type(ob_serializer))
            # ob_serializer = serialize("json", users)
            # return JsonResponse(ob_serializer, safe=False)
        return JsonResponse(ob_serializer.data, safe=False)
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        
        if ob=='Doctor':                       
            user_serializer=UserSerializer(data=user_data)
            if user_serializer.is_valid():
                doctors=Doctor.objects.filter(id_number=user_data['id_number'])
                if len(doctors)==0:
                    user_serializer.save()
                    user_data['user']=user_serializer.data['id']
                    ob_serializer=DoctorSerializer(data=user_data)
                    if ob_serializer.is_valid():                                                                      
                        ob_serializer.save()
                        return JsonResponse(ob_serializer.data, safe=False)
                    else:
                        user=User.objects.get(id=user_data['user_id'])
                        user.delete()                    
                        return JsonResponse(ob_serializer.errors, safe=False)                                            
                else:
                    return JsonResponse("Cédula ya registrada", safe=False)
            else:             
                return JsonResponse(user_serializer.errors, safe=False)
                     
        elif ob=='Paciente':
            ob_serializer = PatientSerializer(data=user_data)

            user_serializer=UserSerializer(data=user_data)
            if user_serializer.is_valid():
                patients=Patient.objects.filter(id_number=user_data['id_number'])
                if len(patients)==0:
                    user_serializer.save()
                    user_data['user']=user_serializer.data['id']
                    ob_serializer=PatientSerializer(data=user_data)
                    if ob_serializer.is_valid():                                                                      
                        ob_serializer.save()
                        return JsonResponse(ob_serializer.data, safe=False)
                    else:
                        user=User.objects.get(id=user_data['user'])
                        user.delete()                    
                        return JsonResponse(ob_serializer.errors, safe=False)                                            
                else:
                    return JsonResponse("Cédula ya registrada", safe=False)
            else:             
                return JsonResponse(user_serializer.errors, safe=False)

        elif ob=='Cita':
            ob_serializer = AppointmentSerializer(data=user_data)
            if ob_serializer.is_valid():
                ob_serializer.save()
                return JsonResponse(ob_serializer.data, safe=False)
            return JsonResponse(ob_serializer.errors, safe=False)

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