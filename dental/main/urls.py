from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('doctors', views.doctors, name='doctors'),
    path('patients', views.patients, name='patients'),
    path('application', views.application, name='application'),
    path('services', views.services, name='services'),
    path('maintenance', views.maintenance, name='maintenance'),
    path('reviews', views.reviews, name='reviews'),
    path('care', views.page1, name='care'),
    path('consultation', views.page2, name='consultation'),
    path('dentistry', views.page3, name='dentistry'),
    path('treatment', views.page4, name='treatment'),
    path('surgery', views.page5, name='surgery'),
    path('prices', views.page6, name='prices')
]