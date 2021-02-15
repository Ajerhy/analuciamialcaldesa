from django import forms
from apps.geolocalizacion.models import Distrito

"""
Constantes
"""

class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = (
            'localidad',
            'numerodistrito',
            'nombredistrito',
            'sigladistrito'
        )
        labels = {
        'numerodistrito': 'Ingrese Numero de Distrito',
        'nombredistrito': 'Ingrese Nombre de Distrito',
        'sigladistrito': 'Ingrese Sigla dle Distrito'}
        widgets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
