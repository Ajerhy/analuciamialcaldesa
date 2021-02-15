from django import forms
from apps.geolocalizacion.models import Provincias

"""
Constantes
"""

class ProvinciasForm(forms.ModelForm):
    class Meta:
        model = Provincias
        fields = (
            'departamentos',
            'nombreprovincias',
            'siglaprovincias')
        labels = {
        'departamentos': 'Ingrese el Departamento',
        'nombreprovincias': 'Ingrese Nombre de Provincia',
        'siglaprovincias': 'Ingrese Sigla Provincia'}
        widgets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
