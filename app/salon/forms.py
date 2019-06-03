from django import forms

from app.salon.models import Salon

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon

        fields = [
            'nombre_salon',
            'estado',
            'conjunto',
        ]

        labels = {
            'nombre_salon': 'Nombre de salon',
            'estado': 'Estado', 
            'conjunto': 'Conjunto',
        }
        widgets = {
            'nombre_salon':forms.TextInput(attrs={'class':'form-control'}),
			'estado':forms.Select(attrs={'class':'form-control'}),
            'conjunto': forms.Select(attrs={'class':'form-control'}),
						
		}