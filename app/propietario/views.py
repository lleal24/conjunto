# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.propietario.forms import PropietarioForm

from app.propietario.models import Propietario
from django.urls import reverse_lazy

#importar vistas del modelo MVC de django crear vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 

# Create your views here.

def index_propietario(request):
    return HttpResponse("Index propietario")


def propietario_view(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('propietario:index_propietario')  
    else:
        form = PropietarioForm()
    return render(request, 'propietario/propietario_form.html', {'form':form})

"""
Esto es lo que se coloca luego de la primera vista
"""
#Vista basada en Clases MVC django predefinidas
class PropietarioList(ListView):
    model = Propietario
    template_name = 'propietario/propietario_list.html'
    ordering = ['numero_identificacion']

class PropietarioCreate(CreateView):
    model = Propietario
    form_class = PropietarioForm

    template_name = 'propietario/propietario_form.html'
    #atributo para urlresolve
    success_url = reverse_lazy('propietario:listar_propietario')

class PropietarioUpdate(UpdateView):
    model = Propietario
    form_class = PropietarioForm
    success_url = reverse_lazy('propietario:listar_propietario')

class PropietarioDelete(DeleteView):
    model = Propietario
    template_name = 'propietario/propietario_delete.html'
    success_url = reverse_lazy('propietario:listar_propietario')