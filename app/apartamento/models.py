# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from app.torre.models import Torre
from app.propietario.models import Propietario
from django.core.validators import RegexValidator


no_validator = RegexValidator("([0-9]){3}", "campo numerico de 3 digitos")

# Create your models here.
class Apartamento(models.Model):
    numero_apartamento = models.TextField(max_length=3, validators=[no_validator])
    fecha_inicio = models.DateField(default=datetime.now)
    fecha_fin = models.DateField(default=datetime.now)
    torre = models.ForeignKey(Torre, null=True, blank=True, on_delete=models.CASCADE)
    propietario = models.ForeignKey(Propietario, null=True, blank=True, on_delete=models.CASCADE)