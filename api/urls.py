from django.urls import re_path, path
from .import views

urlpatterns=[
    re_path(r'^doctor$', views.doctorApi),
    re_path(r'^paciente$', views.patientApi),
    re_path(r'^cita$', views.AppointmentApi),
    re_path(r'^login$', views.login),
    re_path(r'^logout$', views.logout),
    re_path(r'^citas/(?P<fecha>\d{4}-\d{2}-\d{2})/(?P<hora>\d{2}:\d{2}:\d{2})/(?P<doctor_id>[0-9a-f-]+)/$', views.buscar_citas),
    path('cita/<uuid:id>/', views.cita),
    path('paciente/<uuid:id>/', views.paciente),
    path('doctor/<uuid:id>/', views.doctor),
]