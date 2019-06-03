from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.torre.forms import TorreForm

from app.torre.models import Torre
from django.urls import reverse_lazy

#importar vistas del modelo MVC de django crear vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 

# Create your views here.

def index_torre(request):
    return HttpResponse("Index torre")


def torre_view(request):
    if request.method == 'POST':
        form = TorreForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('torre:index_torre')  
    else:
        form = TorreForm()
    return render(request, 'torre/torre_form.html', {'form':form})    
"""
Esto es lo que se coloca luego de la primera vista
"""
#Vista basada en Clases MVC django predefinidas
class TorreList(ListView):
    model = Torre
    template_name = 'torre/torre_list.html'
    ordering = ['id']

class TorreCreate(CreateView):
    model = Torre
    form_class = TorreForm
    template_name = 'torre/torre_form.html'
    #atributo para urlresolve
    success_url = reverse_lazy('torre:listar_torre')

class TorreUpdate(UpdateView):
    model = Torre
    form_class = TorreForm
    success_url = reverse_lazy('torre:listar_torre')

class TorreDelete(DeleteView):
    model = Torre
    template_name = 'torre/torre_delete.html'
    success_url = reverse_lazy('torre:listar_torre')
