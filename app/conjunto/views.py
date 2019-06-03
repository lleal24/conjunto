# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.conjunto.forms import ConjuntoForm
# hasta aqui importes solamente para crear

#import para listar
from app.conjunto.models import Conjunto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 


# Esto va desde el inicio de vista.

def index_conjunto(request):
    return HttpResponse("Index conjunto")

#funcion para crear
def conjunto_view(request):
    if request.method == 'POST':
        form = ConjuntoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('conjunto:index_conjunto')  
    else:
        form = ConjuntoForm()
    return render(request, 'conjunto/conjunto_form.html', {'form':form})

#Vista basada en Clases MVC django predefinidas
class ConjuntoList(ListView):
    model = Conjunto
    template_name = 'conjunto/conjunto_list.html'
    ordering = ['id']

class ConjuntoCreate(CreateView):
    model = Conjunto
    form_class = ConjuntoForm
    template_name = 'conjunto/conjunto_form.html'
    #atributo para urlresolve
    success_url = reverse_lazy('conjunto:listar_conjunto')

class ConjuntoUpdate(UpdateView):
    model = Conjunto
    form_class = ConjuntoForm
    success_url = reverse_lazy('conjunto:listar_conjunto')

class ConjuntoDelete(DeleteView):
    model = Conjunto
    template_name = 'conjunto/conjunto_delete.html'
    success_url = reverse_lazy('conjunto:listar_conjunto')
