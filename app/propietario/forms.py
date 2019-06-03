from django import forms

from app.propietario.models import Propietario

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario

        fields = [
            'numero_identificacion',
            'nombres',
            'apellidos',
            'telefono1',
            'telefono2',
            'celular',
            'correo',
        ]

        labels = {
            'numero_identificacion': 'Numero de identificacion',
            'nombres': 'Nomnbres', 
            'apellidos': 'Apellidos',
            'telefono1': 'Telefono 1',
            'telefono2': 'Telefono 2',
            'celular': 'Celular',
            'correo': 'Correo electronico',
        }
        widgets = {
            'numero_identificacion':forms.TextInput(attrs={'class':'form-control'}),
			'nombres':forms.TextInput(attrs={'class':'form-control'}),
            'apellidos':forms.TextInput(attrs={'class':'form-control'}),
			'telefono1':forms.TextInput(attrs={'class':'form-control'}),
            'telefono2': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
						
		}