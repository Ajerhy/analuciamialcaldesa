from django import forms
from apps.recintos.models import Conteo

class ConteoForm(forms.ModelForm):
   class Meta:
      model = Conteo
      fields = ['sufragio','mesa',
                'totalpapeletas','votovalidos',
                'votonullo','votoblanco',
                'votocc','votojuntos',
                'votocreemos','votomasipsp',
                'votolibre21','votopanbol',
                'votofpv','votoadn',
                'papeletasobreante','carnetssobrantes',
                'ubicacion']
      #fields = '__all__'

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in iter(self.fields):
         self.fields[field].widget.attrs.update({
            'class': 'form-control'
         })