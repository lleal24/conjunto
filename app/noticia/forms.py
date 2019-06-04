from django import forms

from app.noticia.models import Noticia

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia

        fields = [
            'titulo',
            'contenido',
            'conjunto',
            'fecha_inicio',
            'fecha_fin',
            
        ]

        labels = {
            'titulo': 'Titulo',
            'contenido': 'Contenido', 
            'conjunto': 'Conjunto', 
            'fecha_inicio': 'Fecha inicio: yyyy-mm-dd',
            'fecha_fin': 'Fecha fin: yyyy-mm-dd',
       
        }
        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
			'contenido':forms.TextInput(attrs={'class':'form-control'}),
            'conjunto': forms.Select(attrs={'class':'form-control'}),
            'fecha_inicio':forms.DateInput(attrs={'class':'form-control'}),
            'fecha_fin':forms.DateInput(attrs={'class':'form-control'}),
						
		}