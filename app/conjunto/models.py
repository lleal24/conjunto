# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Conjunto(models.Model):
    nombre_conjunto = models.CharField(max_length=50)
    direccion_conjunto = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre_conjunto)
  