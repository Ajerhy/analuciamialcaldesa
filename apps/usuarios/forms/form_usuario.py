from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
from apps.usuarios.models import Usuario
from apps.usuarios.templatetags.utils import ROLES


class UsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Usuario
        fields = 'nombre', 'apellido', 'email','telefono', 'usuario', 'password', 'mesas', 'groups', 'usuario_img'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su email',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su Telefono',
                }
            ),
            'usuario': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su Usuario',
                }
            ),
            'password': forms.PasswordInput(render_value=True,
                attrs={
                    'placeholder': 'Ingrese su password',
                }
            )
            ,
            'mesas': forms.SelectMultiple(attrs={
                'class': 'form-control select2',
                'multiple': 'multiple'
            }),
            'groups': forms.SelectMultiple(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
                'multiple': 'multiple'
            })
        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = Usuario.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
                u.groups.clear()
                for g in self.cleaned_data['groups']:
                    u.groups.add(g)
                u.mesa.clean()
                for m in self.cleaned_data['mesas']:
                    u.groups.add(m)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data





class UsuarioPerfilForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Usuario
        fields = 'nombre', 'apellido', 'email','telefono', 'usuario', 'password', 'usuario_img'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su email',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su Telefono',
                }
            ),
            'usuario': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese su Usuario',
                }
            ),
            'password': forms.PasswordInput(render_value=True,
                                            attrs={
                                                'placeholder': 'Ingrese su password',
                                            }
                                            ),
        }
        exclude = ['user_permissions', 'last_login', 'date_joined', 'is_superuser', 'is_active', 'is_staff', 'groups', 'mesas']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = Usuario.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data