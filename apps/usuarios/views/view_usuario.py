from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView, DetailView, TemplateView, View, DeleteView,ListView)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import json
from apps.usuarios.templatetags.utils import get_ip
from django.db.models import Q
from analuciamialcaldesa import settings
from apps.usuarios.models import Usuario
from apps.usuarios.forms.form_usuario import UsuarioForm
from django.db.models import Sum

USUARIO_FIELDS = [
    {'string': 'N°'},
    {'string': 'Usuario'},
    {'string': 'Email'},
    {'string': 'Grupo'},
    {'string': 'Mesas'},
    {'string': 'Estado'},
    {'string': 'Acciones'},
]

class UsuarioListarView(LoginRequiredMixin,TemplateView):
    model = Usuario
    template_name = "ana/apps/usuarios/usuario/listar.html"
    login_url = 'usuarios:index'

    def get_context_data(self, **kwargs):
        context = super(UsuarioListarView, self).get_context_data(**kwargs)
        usuariotodo = self.model.objects.all()
        usuarioactiva = self.model.objects.exclude(is_active='True')

        context['fields'] = USUARIO_FIELDS
        context["usuario_count"] = usuarioactiva
        context["listar_usuario"] = usuariotodo
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        return context

class UsuarioCrearView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    permission_required = "usuarios.add_usuario"
    model = Usuario
    template_name = "ana/apps/usuarios/usuario/formulario.html"
    #context_object_name = "obj_usuarios"
    form_class = UsuarioForm
    success_url = reverse_lazy("usuarios:listar_usuario")
    success_message = "Usuario Creado Exitosamente"