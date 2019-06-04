# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.empleado.forms import EmpleadoForm

from app.empleado.models import Empleado
from django.urls import reverse_lazy

#importar vistas del modelo MVC de django crear vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 

# Create your views here.

def index_empleado(request):
    return HttpResponse("Index empleado")


def empleado_view(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('empleado:index_empleado')  
    else:
        form = EmpresaForm()
    return render(request, 'empleado/empresa_form.html', {'form':form})

"""
Esto es lo que se coloca luego de la primera vista
"""
#Vista basada en Clases MVC django predefinidas
class EmpleadoList(ListView):
    model = Empleado
    template_name = 'empleado/empleado_list.html'
    ordering = ['numero_identificacion']

class EmpleadoCreate(CreateView):
    model = Empleado
    form_class = EmpleadoForm

    template_name = 'empleado/empleado_form.html'
    #atributo para urlresolve
    success_url = reverse_lazy('empleado:listar_empleado')

class EmpleadoUpdate(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleado:listar_empleado')

class EmpleadoDelete(DeleteView):
    model = Empleado
    template_name = 'empleado/empleado_delete.html'
    success_url = reverse_lazy('empleado:listar_empleado')