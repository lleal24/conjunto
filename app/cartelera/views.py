from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.cartelera.forms import CarteleraForm


from app.cartelera.models import Cartelera
from django.urls import reverse_lazy

#importar vistas del modelo MVC de django crear vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 

# Create your views here.

def index_cartelera(request):
    return HttpResponse("Index cartelera")


def cartelera_view(request):
    if request.method == 'POST':
        form = CarteleraForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('cartelera:index_cartelera')  
    else:
        form = CarteleraForm()
    return render(request, 'cartelera/cartelera_form.html', {'form':form})    
"""
Esto es lo que se coloca luego de la primera vista
"""
#Vista basada en Clases MVC django predefinidas
class CarteleraList(ListView):
    model = Cartelera
    template_name = 'cartelera/cartelera_list.html'
    ordering = ['id']

class CarteleraCreate(CreateView):
    model = Cartelera
    form_class = CarteleraForm
    template_name = 'cartelera/cartelera_form.html'
    #atributo para urlresolve
    success_url = reverse_lazy('cartelera:listar_cartelera')

class CarteleraUpdate(UpdateView):
    model = Cartelera
    form_class = CarteleraForm
    success_url = reverse_lazy('cartelera:listar_cartelera')

class CarteleraDelete(DeleteView):
    model = Cartelera
    template_name = 'cartelera/cartelera_delete.html'
    success_url = reverse_lazy('cartelera:listar_cartelera')


