from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.noticia.forms import NoticiaForm


from app.noticia.models import Noticia
from django.urls import reverse_lazy

#importar vistas del modelo MVC de django crear vistas basadas en clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 

# Create your views here.

def index_noticia(request):
    return HttpResponse("Index noticia")


def noticia_view(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('noticia:index_noticia')  
    else:
        form = NoticiaForm()
    return render(request, 'noticia/noticia_form.html', {'form':form})    
"""
Esto es lo que se coloca luego de la primera vista
"""
#Vista basada en Clases MVC django predefinidas
class NoticiaList(ListView):
    model = Noticia
    template_name = 'noticia/noticia_list.html'
    ordering = ['id']

class NoticiaCreate(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticia/noticia_form.html'
    #atributo para urlresolve
    success_url = reverse_lazy('noticia:listar_noticia')

class NoticiaUpdate(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    success_url = reverse_lazy('noticia:listar_noticia')

class NoticiaDelete(DeleteView):
    model = Noticia
    template_name = 'noticia/noticia_delete.html'
    success_url = reverse_lazy('noticia:listar_noticia')

