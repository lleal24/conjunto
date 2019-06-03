from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.salon.forms import SalonForm

from app.salon.models import Salon
from django.urls import reverse_lazy

#importar vistas del modelo MVC de django crear vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 

# Create your views here.

def index_salon(request):
    return HttpResponse("Index salon")


def salon_view(request):
    if request.method == 'POST':
        form = SalonForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('salon:index_salon')  
    else:
        form = SalonForm()
    return render(request, 'salon/salon_form.html', {'form':form})    
"""
Esto es lo que se coloca luego de la primera vista
"""
#Vista basada en Clases MVC django predefinidas
class SalonList(ListView):
    model = Salon
    template_name = 'salon/salon_list.html'
    ordering = ['id']

class SalonCreate(CreateView):
    model = Salon
    form_class = SalonForm
    template_name = 'salon/salon_form.html'
    #atributo para urlresolve
    success_url = reverse_lazy('salon:listar_salon')

class SalonUpdate(UpdateView):
    model = Salon
    form_class = SalonForm
    success_url = reverse_lazy('salon:listar_salon')

class SalonDelete(DeleteView):
    model = Salon
    template_name = 'salon/salon_delete.html'
    success_url = reverse_lazy('salon:listar_salon')

