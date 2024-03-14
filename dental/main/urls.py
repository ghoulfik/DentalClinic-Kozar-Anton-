from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('doctors', views.doctors, name='doctors'),
    path('patients', views.patients, name='patients'),
    path('application_patients', views.application_patients, name='application_patients'),
    path('application_doctors', views.application_doctors, name='application_doctors')
]