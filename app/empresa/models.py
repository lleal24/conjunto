# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.conjunto.models import Conjunto
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.core.validators import RegexValidator

NIT_validator = RegexValidator("([0-9]){13}", "NIT debe ser numerico de 13 caracteres")
tel_validator = RegexValidator("([0-9]){7}", "campo numerico de 7 digitos")
cel_validator = RegexValidator("([0-9]){10}", "campo numerico de 10 digitos")

# Create your models here.
class Empresa(models.Model):
    ESTADO = (
        ('A', 'Activa'),
        ('I', 'Inactiva'),
    )

    NIT = models.TextField(validators=[NIT_validator], primary_key=True)
    razon_social = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.TextField(validators=[tel_validator] ,blank=True)
    celular = models.TextField(validators=[cel_validator])
    estado= models.CharField(max_length=1, choices=ESTADO)
    fecha_inicio = models.DateField(default=datetime.now)
    fecha_fin = models.DateField(default=datetime.now)
    conjunto = models.ForeignKey(Conjunto, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.razon_social)