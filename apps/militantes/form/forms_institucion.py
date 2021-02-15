from django import forms
from apps.militantes.models import Institucion


"""
Constantes
"""

class InstitucionForm(forms.ModelForm):

    class Meta:
        model = Institucion
        fields = ['nombreinstitucion','siglainstitucion','nitinstitucion']
        labels = {'nombreinstitucion': "Nombre Institucion",
                  "siglainstitucion": "Sigla Institucion",
                  "nitinstitucion": "NIT Institucion"}

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_nombreinstitucion(self):
        ni = self.cleaned_data['nombreinstitucion']
        num_palabras = len(ni)
        if num_palabras < 4:
            raise forms.ValidationError("Nombre Institucion muy corto")
        return ni

    def clean_nitinstitucion(self):
        nit = self.cleaned_data['nitinstitucion']
        institucion = Institucion.objects.filter(nitinstitucion__iexact=nit).exclude(id=self.instance.id)
        if institucion:
            raise forms.ValidationError("este NIT ya esta Registrado")
        else:
            return nit