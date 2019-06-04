# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.core.validators import RegexValidator

from app.conjunto.models import Conjunto


text_validator = RegexValidator("([A-Z])\w+", "campo solo admite letras")



# Create your models here.
class Evento(models.Model):
    titulo = models.TextField(max_length=45, validators=[text_validator])
    contenido = models.TextField(max_length=254, validators=[text_validator])
    conjunto = models.ForeignKey(Conjunto, null=True, blank=True, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=datetime.now)
    fecha_fin = models.DateField(default=datetime.now)
    
 
 
