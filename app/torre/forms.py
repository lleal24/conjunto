from django import forms

from app.torre.models import Torre

class TorreForm(forms.ModelForm):
    class Meta:
        model = Torre

        fields = [
            'nombre_torre',
            'numero_pisos',
            'conjunto',
        ]

        labels = {
            'nombre_torre': 'Nombre de torre',
            'numero_pisos': 'Numero de pisos', 
            'conjunto': 'Conjunto',
        }
        widgets = {
            'nombre_torre':forms.TextInput(attrs={'class':'form-control'}),
			'numero_pisos':forms.TextInput(attrs={'class':'form-control'}),
            'conjunto': forms.Select(attrs={'class':'form-control'}),
						
		}