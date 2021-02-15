from django import forms
from apps.geolocalizacion.models import Localidad

class LocalidadFrom(forms.ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
