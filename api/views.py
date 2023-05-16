from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from api.models import *
from api.serializers import *
# Create your views here.


def CRUD(request, ob):
    if not (request.method == 'POST' and (ob == 'Doctor' or ob == 'Paciente')):
        try:
            user_auth_tuple = TokenAuthentication().authenticate(request)
        except:
            return JsonResponse("Usuario no autenticado", status=401, safe=False)
        if user_auth_tuple is None:
            return JsonResponse("Usuario no autenticado", status=401, safe=False)

    if request.method == 'GET':
        (usuario, token) = user_auth_tuple  # here come your user object
        if ob == 'Doctor':
            users = Doctor.objects.all()
            # for user in users:
            #     print(user.schedule['miercoles'])
        elif ob == 'Paciente':
            users = Patient.objects.all()
        elif ob == 'Cita':
            users = Appointment.objects.all()
            # for user in users:
            #     print(user.date.weekday())
            #     print(user.time)
            #     t1="8:00-18:00".split("-")
            #     ini=t1[0].split(":")
            #     fin=t1[1].split(":")
            #     print(ini," ",fin)
            #     time2=user.time.replace(hour=int(ini[0]), minute=int(ini[1]), second=0, microsecond=0)
            #     print(user.time>time2)
        try:
            data = JSONParser().parse(request)
        except:
            data = {}
        try:
            if data:
                if ob == 'Doctor':
                    users = Doctor.objects.filter(id_number=data['id_number'])
                elif ob == 'Paciente':
                    users = Patient.objects.filter(id_number=data['id_number'])
                elif ob == 'Cita':
                    if (len(Doctor.objects.filter(_id=data['id'])) != 0):
                        users = Appointment.objects.filter(doctor=data['id'])
                    else:
                        users = Appointment.objects.filter(patient=data['id'])
        except:
            data = {}
        if ob == 'Doctor':
            ob_serializer = DoctorSerializer(users, many=True)
        elif ob == 'Paciente':
            ob_serializer = PatientSerializer(users, many=True)
        elif ob == 'Cita':
            ob_serializer = AppointmentSerializer(users, many=True)
        return JsonResponse(ob_serializer.data, safe=False)

    if request.method == 'POST':
        user_data = JSONParser().parse(request)

        if ob == 'Doctor':
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                doctors = Doctor.objects.filter(
                    id_number=user_data['id_number'])
                if len(doctors) == 0:
                    user_serializer.save()
                    user_data['user'] = user_serializer.data['id']
                    ob_serializer = DoctorSerializer(data=user_data)
                    if ob_serializer.is_valid():
                        ob_serializer.save()
                        return JsonResponse(ob_serializer.data, safe=False)
                    else:
                        user = User.objects.get(id=user_data['user_id'])
                        user.delete()
                        return JsonResponse(ob_serializer.errors, status=400, safe=False)
                else:
                    return JsonResponse("Cédula ya registrada", status=400, safe=False)
            else:
                return JsonResponse(user_serializer.errors, status=400, safe=False)

        elif ob == 'Paciente':
            ob_serializer = PatientSerializer(data=user_data)

            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                patients = Patient.objects.filter(
                    id_number=user_data['id_number'])
                if len(patients) == 0:
                    user_serializer.save()
                    user_data['user'] = user_serializer.data['id']
                    ob_serializer = PatientSerializer(data=user_data)
                    if ob_serializer.is_valid():
                        ob_serializer.save()
                        return JsonResponse(ob_serializer.data, safe=False)
                    else:
                        user = User.objects.get(id=user_data['user'])
                        user.delete()
                        return JsonResponse(ob_serializer.errors, status=400, safe=False)
                else:
                    return JsonResponse("Cédula ya registrada", status=400, safe=False)
            else:
                return JsonResponse(user_serializer.errors, status=400, safe=False)

        elif ob == 'Cita':
            ob_serializer = AppointmentSerializer(data=user_data)
            if ob_serializer.is_valid():
                ob_serializer.save()
                return JsonResponse(ob_serializer.data, safe=False)
            return JsonResponse(ob_serializer.errors, status=400, safe=False)


@csrf_exempt
def doctorApi(request):
    return CRUD(request, "Doctor")


@csrf_exempt
def patientApi(request):
    return CRUD(request, "Paciente")


@csrf_exempt
def AppointmentApi(request, id=0):
    return CRUD(request, "Cita")


@csrf_exempt
def medicalApi(request):
    if request.method == "GET":
        medical = History.objects.all()
        data = JSONParser().parse(request)
        if data['_id']:
            medical = History.objects.filter(_id=data['_id'])
        History_serializer = historySerializer(medical, many=True)
        return JsonResponse(History_serializer.data, safe=False)


@csrf_exempt
def cita(request, id):
    if request.method=='GET':
        try:
            user_auth_tuple = TokenAuthentication().authenticate(request)
        except:
            return JsonResponse("Usuario no autenticado", status=401, safe=False)
        if user_auth_tuple is None:
            return JsonResponse("Usuario no autenticado", status=401, safe=False)
        if (len(Doctor.objects.filter(_id=id)) != 0):
            citas = Appointment.objects.filter(doctor=id)
            resp=[]
            doc=Doctor.objects.get(_id=id)
            for cita in citas:
                pat=Patient.objects.get(_id=cita.patient._id)
                resp.append({
                    "patient":pat.name,
                    "doctor":doc.name,
                    "address":pat.address,
                    "id_number":pat.id_number,
                    "phone_number":pat.phone_number,
                    "specialization":doc.specialization,
                    "date":cita.date,
                    "time":cita.time  
                    })
        else:
            citas=Appointment.objects.filter(patient=id)
            resp=[]
            pat=Patient.objects.get(_id=id)
            for cita in citas:
                doc=Doctor.objects.get(_id=cita.doctor._id)
                resp.append({
                    "patient":pat.name,
                    "doctor":doc.name,
                    "address":doc.address,
                    "phone_number":doc.phone_number,
                    "specialization":doc.specialization,
                    "id_number":doc.id_number,
                    "date":cita.date,
                    "time":cita.time                    
                    })        
        return JsonResponse(resp, safe=False, status=200)
    else:
        return JsonResponse("Metodo no permitido", safe=False, status=404)

@csrf_exempt
def login(request):
    if request.method=="POST":
        user_data = JSONParser().parse(request)
        username=user_data['username']
        password=user_data['password']        
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse("Usuario invalido", status=404, safe=False)
        pwd_valid=check_password(password, user.password)
        if not pwd_valid:
            return JsonResponse("Contraseña incorrecta", status=400, safe=False)
        token, _=Token.objects.get_or_create(user=user)
        
        
        if(len(Doctor.objects.filter(user=user))==0):
            op="paciente"
            pat=Patient.objects.get(user=user)
            id=pat._id
        else:
            op="doctor"
            doc=Doctor.objects.get(user=user)
            id=doc._id
        return JsonResponse({"token":token.key, "op":op, "id":id}, status=200, safe=False)
    else:
        return JsonResponse("Solo se permite el metodo post", status=400, safe=False)


@csrf_exempt
def logout(request):
    user_auth_tuple = TokenAuthentication().authenticate(request)
    if user_auth_tuple is None:
        return JsonResponse("Usuario no autenticado",status=401, safe=False)
    else:
        (usuario, token) = user_auth_tuple # here come your user object
        token.delete()
        return JsonResponse(f"Sesion de Usuario {usuario} cerrada",status=200, safe=False)