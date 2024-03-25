from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.

class NewsDeleteView (DeleteView):
    model = Artiles
    success_url='/patients'
    template_name = 'main/info-delete.html'


class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'main/application.html'
    form_class = ArtilesForm
    #fields = ['title','num','address','date','info']

class NewsDetailView(DetailView):
    model=Artiles
    template_name = 'main/details_view.html'
    context_object_name = 'article'

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

def services(request):
    return render(request, 'main/services.html')

def maintenance(request):
    return render(request, 'main/maintenance.html')

def reviews(request):
    return render(request, 'main/reviews.html')

def page1(request):
    return render(request, 'main/services/page1.html')

def page2(request):
    return render(request, 'main/services/page2.html')

def page3(request):
    return render(request, 'main/services/page3.html')

def page4(request):
    return render(request, 'main/services/page4.html')

def page5(request):
    return render(request, 'main/services/page5.html')

def page6(request):
    return render(request, 'main/services/page6.html')