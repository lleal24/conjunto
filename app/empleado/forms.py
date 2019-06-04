from django import forms

from app.empleado.models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado

        fields = [
            'numero_identificacion',
            'nombres',
            'apellidos',
            'direccion',
            'telefono1',
            'telefono2',
            'celular',
            'estado',
            'empresa',
        ]

        labels = {
            'numero_identificacion': 'Numero de identificacion',
            'nombres': 'Nomnbres', 
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'telefono1': 'Telefono 1',
            'telefono2': 'Telefono 2',
            'celular': 'Celular',
            'estado': 'Estado',
            'empresa': 'Empresa',
        }
        widgets = {
            'numero_identificacion':forms.TextInput(attrs={'class':'form-control'}),
			'nombres':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
			'telefono1':forms.TextInput(attrs={'class':'form-control'}),
            'telefono2': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'empresa': forms.Select(attrs={'class':'form-control'}),
						
		}