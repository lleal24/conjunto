# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from app.apartamento.forms import ApartamentoForm

from app.apartamento.models import Apartamento
from django.urls import reverse_lazy

#importar vistas del modelo MVC de django crear vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 

# Create your views here.

def index_apartamento(request):
    return HttpResponse("Index apartamento")


def apartamento_view(request):
    if request.method == 'POST':
        form = ApartamentoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('apartamento:index_apartamento')  
    else:
        form = ApartamentoForm()
    return render(request, 'apartamento/apartamento_form.html', {'form':form}) 
"""
Esto es lo que se coloca luego de la primera vista
"""
#Vista basada en Clases MVC django predefinidas
class ApartamentoList(ListView):
    model = Apartamento
    template_name = 'apartamento/apartamento_list.html'
    ordering = ['id']

class ApartamentoCreate(CreateView):
    model = Apartamento
    form_class = ApartamentoForm
    template_name = 'apartamento/apartamento_form.html'
    #atributo para urlresolve
    success_url = reverse_lazy('apartamento:listar_apartamento')

class ApartamentoUpdate(UpdateView):
    model = Apartamento
    form_class = ApartamentoForm
    success_url = reverse_lazy('apartamento:listar_apartamento')

class ApartamentoDelete(DeleteView):
    model = Apartamento
    template_name = 'apartamento/apartamento_delete.html'
    success_url = reverse_lazy('apartamento:listar_apartamento')