from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.evento.forms import EventoForm


from app.evento.models import Evento
from django.urls import reverse_lazy

#importar vistas del modelo MVC de django crear vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 

# Create your views here.

def index_evento(request):
    return HttpResponse("Index evento")


def evento_view(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('evento:index_evento')  
    else:
        form = EventoForm()
    return render(request, 'evento/evento_form.html', {'form':form})    
"""
Esto es lo que se coloca luego de la primera vista
"""
#Vista basada en Clases MVC django predefinidas
class EventoList(ListView):
    model = Evento
    template_name = 'evento/evento_list.html'
    ordering = ['id']

class EventoCreate(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento/evento_form.html'
    #atributo para urlresolve
    success_url = reverse_lazy('evento:listar_evento')

class EventoUpdate(UpdateView):
    model = Evento
    form_class = EventoForm
    success_url = reverse_lazy('evento:listar_evento')

class EventoDelete(DeleteView):
    model = Evento
    template_name = 'evento/evento_delete.html'
    success_url = reverse_lazy('evento:listar_evento')
