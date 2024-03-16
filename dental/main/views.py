from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def doctors(request):
    return render(request, 'main/doctors.html')

def patients(request):
    info=Artiles.objects.order_by('date')
    return render(request, 'main/patients.html', {'info':info})

def application(request):
    error=""
    if request.method=="POST":
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
        else:
            error="Форма невірна"

    form=ArtilesForm()
    data={
        'form':form,
        'error':error


    }
    return render(request, 'main/application.html', data)