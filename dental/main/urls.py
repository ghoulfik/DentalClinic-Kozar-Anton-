from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('doctors', views.doctors, name='doctors'),
    path('patients', views.patients, name='patients'),
    path('application', views.application, name='application')
]