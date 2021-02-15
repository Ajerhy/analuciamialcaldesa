from django import forms
from apps.geolocalizacion.models import Barrio

"""
Constantes
"""

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ('distrito',
                  'nombrebarrio',
                  'siglabarrio',
                  'detallebarrio')
        labels = {
            'distrito': 'Ingrese el Distrito',
            'nombrebarrio': 'Ingrese Nombre Barrio',
            'siglabarrio': 'Ingrese Sigla de Barrio',
            'detallebarrio': 'Ingrese Detalle del Barrio'}
        widgets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
