from django.urls import re_path
from .import views

urlpatterns=[
    re_path(r'^doctor$', views.doctorApi),
    re_path(r'^paciente$', views.patientApi),
    re_path(r'^cita$', views.AppointmentApi),
    re_path(r'^login$', views.login),
    re_path(r'^logout$', views.logout),
]