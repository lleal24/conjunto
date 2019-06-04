# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from app.usuario.forms import RegistroForm

# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('usuario:listar_usuario')

class UsuarioList(ListView):
    model = User
    template_name = 'usuario/usuario_list.html'

class UsuarioUpdate(UpdateView):
    model = User
    form_class = RegistroForm
    success_url = reverse_lazy('usuario:listar_usuario') 

class UsuarioDelete(DeleteView):
    model = User
    template_name = 'usuario/usuario_delete.html'
    success_url = reverse_lazy('usuario:listar_usuario')