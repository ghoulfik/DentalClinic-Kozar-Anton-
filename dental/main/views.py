from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def doctors(request):
    return render(request, 'main/doctors.html')

def patients(request):
    return render(request, 'main/patients.html')

def application(request):
    return render(request, 'main/application.html')