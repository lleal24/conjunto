# -*MODELO EMPLEADO*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.core.validators import RegexValidator #Validador de expresiones regulares
from app.empresa.models import Empresa #Relacion de uno a mucho con empresa

id_validator = RegexValidator("([0-9]){8,11}", "campo numerico de almenos 8 digitos max 11")
tel_validator = RegexValidator("([0-9]){7}", "campo numerico de 7 digitos")
cel_validator = RegexValidator("([0-9]){10}", "campo numerico de 10 digitos")
text_validator = RegexValidator("([A-Z])\w+", "campo solo admite letras")



# Create your models here.
class Empleado(models.Model):
    ESTADO = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )

    numero_identificacion = models.TextField(max_length=11, validators=[id_validator], primary_key=True)
    nombres = models.TextField(max_length=45, validators=[text_validator])
    apellidos = models.TextField(max_length=45, validators=[text_validator])
    direccion = models.TextField(max_length=45)
    telefono1 = models.TextField(max_length=7, validators=[tel_validator])
    telefono2 = models.TextField(max_length=7, validators=[tel_validator],blank=True)
    celular = models.TextField(max_length=10, validators=[cel_validator])
    correo = models.EmailField(max_length=45)
    estado= models.CharField(max_length=1, choices=ESTADO)
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.CASCADE)
 
