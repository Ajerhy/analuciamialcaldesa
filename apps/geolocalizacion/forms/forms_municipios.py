from django import forms
from apps.geolocalizacion.models import Municipios

"""
Constantes
"""

class MunicipiosForm(forms.ModelForm):
    class Meta:
        model = Municipios
        fields = (
            'provincias',
            'nombremunicipios',
            'siglamunicipios',
        )
        labels = {
            'provincias': 'Ingrese la Provincia',
            'nombremunicipios': 'Ingrese Nombre del Municipio',
            'siglamunicipios': 'Ingrese Sigla del Municipio'}
        widgets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
