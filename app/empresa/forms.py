from django import forms

from app.empresa.models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa

        fields = [
            'NIT',
            'razon_social',
            'direccion',
            'telefono',
            'celular',
            'estado',
            'fecha_inicio',
            'fecha_fin',
            'conjunto',
        ]

        labels = {
            'NIT': 'NIT',
            'razon_social': 'Razon social', 
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'celular': 'Celular',
            'estado': 'Estado',
            'fecha_inicio': 'Temporalidad inicio',
            'fecha_fin': 'Temporalidad fin',
            'conjunto': 'Conjunto',
        }
        widgets = {
            'NIT':forms.TextInput(attrs={'class':'form-control'}),
			'razon_social':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'conjunto': forms.Select(attrs={'class':'form-control'}),
						
		}