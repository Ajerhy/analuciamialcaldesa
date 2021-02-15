from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
from apps.usuarios.models import Usuario
from apps.usuarios.templatetags.utils import ROLES

ERROR_MESSAGE_USUARIO = {'required':'El usuario es requerido','unique':'El usuario ya se encuentra registrado','invalid': 'Ingrese el usuario valido'}
ERROR_MESSAGE_PASSWORD = {'required':'El password es requerido'}
ERROR_MESSAGE_EMAIL = {'required':'el email es requerido','invalid':'Ingrese un correo valido'}

def must_be_gt(value_password):
    if len(value_password) < 7:
        raise forms.ValidationError('El Password debe tener mas de 8 Caracter')

def must_a_gt(value_password):
    if len(value_password) < 8:
        raise forms.ValidationError('El Password debe Caracteres Validos')


#Login
class LoginForm(forms.ModelForm):
    usuario = forms.CharField(max_length= 15)
    password = forms.CharField(max_length= 15,widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['usuario', 'password']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if len(password) < 4:
                raise forms.ValidationError("¡La contraseña debe tener al menos 8 caracteres!")
        return password

    def clean(self):
        usuario = self.cleaned_data.get("usuario")
        password = self.cleaned_data.get("password")

        if usuario and password:
            self.user = authenticate(usuario=usuario, password=password)
            if self.user:
                if not self.user.is_active:
                    pass
                    #raise forms.ValidationError("El usuario esta Inactivo")
            else:
                pass
                #raise forms.ValidationError("Usuario y Contraseña no válidos")
        return self.cleaned_data
