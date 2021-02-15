from django import forms
from apps.candidatos.models import Candidato

class CandidatoForm(forms.ModelForm):
   class Meta:
      model = Candidato
      fields = ['titulo','cargo',
                'frase','imagen']
      #fields = '__all__'

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for field in iter(self.fields):
         self.fields[field].widget.attrs.update({
            'class': 'form-control'
         })