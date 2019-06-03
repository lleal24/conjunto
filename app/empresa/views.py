# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.empresa.forms import EmpresaForm

from app.empresa.models import Empresa
from django.urls import reverse_lazy

#importar vistas del modelo MVC de django crear vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 

# Create your views here.

def index_empresa(request):
    return HttpResponse("Index empresa")


def empresa_view(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('empresa:index_empresa')  
    else:
        form = EmpresaForm()
    return render(request, 'empresa/empresa_form.html', {'form':form})

"""
Esto es lo que se coloca luego de la primera vista
"""
#Vista basada en Clases MVC django predefinidas
class EmpresaList(ListView):
    model = Empresa
    template_name = 'empresa/empresa_list.html'
    ordering = ['NIT']

class EmpresaCreate(CreateView):
    model = Empresa
    form_class = EmpresaForm

    template_name = 'empresa/empresa_form.html'
    #atributo para urlresolve
    success_url = reverse_lazy('empresa:listar_empresa')

class EmpresaUpdate(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    success_url = reverse_lazy('empresa:listar_empresa')

class EmpresaDelete(DeleteView):
    model = Empresa
    template_name = 'empresa/empresa_delete.html'
    success_url = reverse_lazy('empresa:listar_empresa')