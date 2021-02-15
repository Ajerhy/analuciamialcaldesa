from django import forms
from apps.recintos.models import Conteo

class PapeletaForm(forms.ModelForm):
   class Meta:
      model = Conteo
      fields = ['sufragio','mesa',
                'totalpapeletas','votovalidos',
                'votonullo','votoblanco',
                'votopst', 'votopaso', 'votopanbol', 'votocid', 'votomda', 'votomts', 'votovida', 'votomasipsp',
                'papeletasobreante','carnetssobrantes',
                'ubicacion']
      #fields = '__all__'

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in iter(self.fields):
         self.fields[field].widget.attrs.update({
            'class': 'form-control'
         })