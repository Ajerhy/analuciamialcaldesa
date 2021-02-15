from django import forms
from apps.geolocalizacion.models import Departamentos

"""
Constantes
"""

class DepartamentosForm(forms.ModelForm):
    class Meta:
        model = Departamentos
        fields = (
            'nombredepartamentos',
            'sigladepartamentos',)
        labels = {
        'nombredepartamentos': 'Ingrese Nombre del Departamento',
        'sigladepartamentos': 'Ingrese Sigla del Departamento'}
        widgets = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
