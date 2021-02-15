from django import forms
from apps.geolocalizacion.models import Direccion

"""
Constantes
"""

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ('ubicacion',
                  'barrio',
                  'zonadireccion',
                  'referenciadireccion',
                  'viadireccion',
                  'calledireccion',
                  'numerocasadireccion',
                  'avenidadireccion')
        labels = {
            'ubicacion': 'Ingrese Ubicacion',
            'barrio': 'Ingrese el Barrio',
            'zonadireccion': 'Ingrese Zona',
            'referenciadireccion': 'Ingrese Referencia',
            'viadireccion': 'Ingrese Via',
            'calledireccion': 'Ingrese Calle',
            'numerocasadireccion': 'Ingrese Numero de Casa',
            'avenidadireccion': 'Ingrese Nombre de Avenida'}
        widgets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
