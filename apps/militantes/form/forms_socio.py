from django import forms
from apps.militantes.models import Socio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
