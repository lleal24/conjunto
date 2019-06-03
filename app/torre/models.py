# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.conjunto.models import Conjunto
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator

piso_validator = RegexValidator("([0-9]){1}", "campo numerico de 1 digito")

# Create your models here.
class Torre(models.Model):
    nombre_torre = models.CharField(max_length=50)
    numero_pisos = models.TextField(max_length=1, validators=[piso_validator])
    conjunto = models.ForeignKey(Conjunto, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_torre)
