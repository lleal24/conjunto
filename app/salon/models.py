# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.conjunto.models import Conjunto
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Salon(models.Model):
    ESTADO = (
        ('D', 'Disponible'),
        ('N', 'No disponible'),
    )
    nombre_salon= models.CharField(max_length=50)
    estado= models.CharField(max_length=1, choices=ESTADO)
    conjunto = models.ForeignKey(Conjunto, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_torre)