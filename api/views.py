from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from api.models import Users, Institutions
from api.serializers import UserSerializer, InstitutionSerializer
# Create your views here.


@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Registrado exitosamente", safe=False)
        return JsonResponse("Fallo al registrarse", safe=False)
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user=Users.objects.get(UserId=user_data['UserId'])
        users_serializer=UserSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Actualizado exitosamente", safe=False)
        return JsonResponse("Fallo al actualizar", safe=False)
    elif request.method=='DELETE':
        user = Users.objects.get(UserId=id)
        if user:
            user.delete()
            return JsonResponse("Eliminado exitosamente", safe=False)
        else:
            return JsonResponse("Usuario no encontrado", safe=False)

# def getRoutes(request):
#     #Rutas de prueba
#     routes = [
#         {
#             'Endpoint': '/notes/',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of notes'
#         },
#         {
#             'Endpoint': '/notes/id',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns a single note object'
#         },
#         {
#             'Endpoint': '/notes/create/',
#             'method': 'POST',
#             'body': {'body': ""},
#             'description': 'Creates new note with data sent in post request'
#         },
#         {
#             'Endpoint': '/notes/id/update/',
#             'method': 'PUT',
#             'body': {'body': ""},
#             'description': 'Creates an existing note with data sent in post request'
#         },
#         {
#             'Endpoint': '/notes/id/delete/',
#             'method': 'DELETE',
#             'body': None,
#             'description': 'Deletes and exiting note'
#         },
#     ]
#     return JsonResponse(routes, safe=False)
