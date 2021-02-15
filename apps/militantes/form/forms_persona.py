from django import forms
from django.forms import ModelForm
from apps.militantes.models import Persona

"""
Constantes
"""

ERROR_MESSAGE_CI = {'required':'El numero de cedula de identidad es requerido','unique':'El numero de cedula de identidad ya se encuentra registrado','invalid': 'Ingrese el numero de cedula de identidad valido'}
#SEXOS = (('1', 'Hombre'),('0', 'Mujer'))
SEXOS = ((True, 'Hombre'),(False, 'Mujer'))
FORMATO_FECHA = ['%Y-%m-%d']

def get_ci(value_generopersona):
    if len(value_generopersona) < 6:
        raise forms.ValidationError('Numero de Cedula de Identidad debe tener mas de 6 Caracter')


    """
    nombrepersona = form.CharField(max_length=20,label='Nombre',widget=form.TextInput(attrs={'class': 'form-control',}))
    paternopersona = form.CharField(max_length=20,label='Apellido Materno',widget=form.TextInput(attrs={'class': 'form-control',}))
    maternopersona = form.CharField(max_length=20,label='Apellido Paterno',widget=form.TextInput(attrs={'class': 'form-control',}))
    cipersona = form.CharField(max_length=20,label='Cedula Identidad',widget=form.TextInput(attrs={'class': 'form-control'}))
    generopersona1 = form.CharField(label='Sexo',widget=form.Select(choices=SEXOS,attrs={'class':'form-control'}))

    nacimientopersona = form.DateField(label='Fecha de Nacimiento',widget=form.DateInput(attrs={
        'class':'form-control',
        'maxlength':'10'
    }),input_formats=FORMATO_FECHA)
    """

class PersonaForm(forms.ModelForm):
    nombrepersona = forms.CharField(max_length=50,label='Nombre')
    paternopersona = forms.CharField(max_length=90,label='Apellido Paterno',required=False)
    maternopersona = forms.CharField(max_length=90,label='Apellido Materno',required=False)
    cipersona = forms.CharField(max_length=20,label='Cedula de Identidad',validators = [get_ci])

    class Meta:
        model = Persona
        fields = ['nombrepersona','paternopersona','maternopersona',
                  'cipersona','generopersona','nacimientopersona']

        labels = {'generopersona': 'Genero',
                  'nacimientopersona': 'Fecha de Nacimiento'}
        widgets = {
        'nacimientopersona' : forms.DateInput(attrs={'type': 'text'}),
        'generopersona': forms.Select(choices=SEXOS)
        }
#'type': 'date'
    def clean_cipersona(self):
        ci = self.cleaned_data['cipersona']
        persona = Persona.objects.filter(cipersona__iexact=ci).exclude(id=self.instance.id)
        if persona:
            raise forms.ValidationError("El Numero de Cedula de Identidad Ya Existe")
        else:
            return ci

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

"""
    def clean_nombrepersona(self):
        nombrepersona = self.cleaned_data['nombrepersona']
        if not nombrepersona.isalpha():
            raise form.ValidationError('Este Campo No puede contener Números')
        return nombrepersona
"""