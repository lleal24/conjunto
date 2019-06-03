from django import forms

from app.conjunto.models import Conjunto

class ConjuntoForm(forms.ModelForm):
    class Meta:
        model = Conjunto

        fields = [
            'nombre_conjunto',
            'direccion_conjunto',
        ]

        labels = {
            'nombre_conjunto': 'Nombre de conjunto',
            'direccion_conjunto': 'Direccion', 
        }
        widgets = {
			'nombre_conjunto':forms.TextInput(attrs={'class':'form-control'}),
			'direccion_conjunto':forms.TextInput(attrs={'class':'form-control'}),
			
		}