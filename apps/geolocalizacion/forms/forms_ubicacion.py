from django import forms
from apps.geolocalizacion.models import Ubicacion

"""
Constantes
"""

class UbicacionForm(forms.ModelForm):
    #latitudubicacion = forms.CharField(label='Latitud',disabled=True)
    #longitudubicacion = forms.CharField(label='Longitud',disabled=True)
    class Meta:
        model = Ubicacion
        fields = ('latitudubicacion',
                  'longitudubicacion',
                  'descripcionubicacion'
                  )
        labels = {
            'latitudubicacion': 'Ingrese la Latitud',
            'longitudubicacion': 'Ingrese la Longitud',
            'descripcionubicacion': 'Ingrese la Descripcion'}
        widgets = {
            'descripcionubicacion': forms.Textarea(attrs={
                'cols': 10, 'rows': 5, 'placeholder': 'Ingrese detalle Observacion',
                'class': 'border border-info'})
            #,'latitudubicacion':forms.TextInput(attrs={'disabled':True})
            #,'longitudubicacion': forms.TextInput(attrs={'disabled': True})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
