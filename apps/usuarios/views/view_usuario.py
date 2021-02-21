from django.shortcuts import render
#from django.views.generic import (CreateView, UpdateView, DetailView, TemplateView, View, DeleteView,ListView)
from django.views import generic
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
from apps.usuarios.forms.form_usuario import UsuarioForm,UsuarioPerfilForm
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

class UsuarioListarView(LoginRequiredMixin,generic.TemplateView):
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

class UsuarioCrearView(SuccessMessageMixin,LoginRequiredMixin,generic.CreateView):
    login_url = 'usuarios:index'
    #permission_required = "usuarios.add_usuario"
    model = Usuario
    template_name = "ana/apps/usuarios/usuario/formulario.html"
    context_object_name = "obj"
    form_class = UsuarioForm
    success_url = reverse_lazy("usuarios:listar_usuario")
    success_message = "Usuario Creado Exitosamente"

class UsuarioEditarView(SuccessMessageMixin,LoginRequiredMixin,generic.UpdateView):
    login_url = 'usuarios:index'
    model = Usuario
    template_name = "ana/apps/usuarios/usuario/formulario.html"
    context_object_name = "obj"
    form_class = UsuarioForm
    success_url = reverse_lazy("usuarios:listar_usuario")
    success_message = "Usuario Actualizado Satisfactoriamente"
    #permission_required = "usuarios.change_usuario"

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

class UsuarioEliminarView(SuccessMessageMixin, LoginRequiredMixin, generic.DeleteView):
    #permission_required = "inv.delete_categoria"
    model = Usuario
    template_name = 'ana/apps/usuarios/usuario/eliminar.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("usuarios:listar_usuario")
    success_message = "Usuario Eliminada Satisfactoriamente"

    """
    def get_context_data(self, **kwargs):
        context = super(UsuarioEditarView, self).get_context_data(**kwargs)
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        return context

    def form_valid(self, form):
        Usuario = form.save(commit=False)
        #persona.um = self.request.user.id
        Usuario.direccion_ip = get_ip(self.request)
        Usuario.save()
        return super().form_valid(form)
"""

class UsuarioPerfilView(LoginRequiredMixin, generic.UpdateView):
    model = Usuario
    form_class = UsuarioPerfilForm
    template_name = 'ana/apps/usuarios/usuario/perfil.html'
    success_url = reverse_lazy('usuarios:dashboard')
