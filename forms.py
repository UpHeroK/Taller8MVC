from django import forms 
from .models import*

class CiudadForm(forms.ModelForm):
    class Meta:
        model = ciudad
        fields = [
            'idciudad',
            'nombredciudad',
            'descripcionciudad',
        ]

class PersonaForm(forms.ModelForm):
    class Meta:
        model = persona
        fields = [
            'idp',
            'nombres',
            'apellidos',
            'idtipdoc',
            'documentop',
            'lugarderesi',
            'email',
            'tel',
            'usuario',
            'password',
        ]
        
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = documento
        fields = [
            'idoc',
            'nombredoc',
            'descripciondoc',
        ]