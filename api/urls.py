from django.urls import re_path
from .import views

urlpatterns=[
    re_path(r'^user$', views.userApi),
    re_path(r'^user/([0-9]+)$', views.userApi),
    re_path(r'^doctor$', views.doctorApi),
    re_path(r'^paciente$', views.patientApi),
    re_path(r'^cita$', views.AppointmentApi),
]