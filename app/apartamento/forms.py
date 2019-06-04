from django import forms


from app.apartamento.models import Apartamento

class ApartamentoForm(forms.ModelForm):
    class Meta:
        model = Apartamento

        fields = [
            'numero_apartamento',
            'fecha_inicio',
            'fecha_fin',
            'torre',
            'propietario',
        ]

        labels = {
            'numero_apartamento': 'Numero de apartamento',
            'fecha_inicio': 'Temporalidad inicio',
            'fecha_fin': 'Temporalidad fin', 
            'torre': 'Torre',
            'propietario': 'Propietario',
        }
        widgets = {
			'numero_apartamento':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_inicio':forms.DateInput(attrs={'class':'form-control'}),
            'fecha_fin':forms.DateInput(attrs={'class':'form-control'}),
            'torre': forms.Select(attrs={'class':'form-control'}),
            'propietario': forms.Select(attrs={'class':'form-control'}),

        

			
		}