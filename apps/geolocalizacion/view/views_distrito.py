from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView, DetailView, TemplateView, View, DeleteView,ListView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import json
from apps.usuarios.templatetags.utils import get_ip
from django.db.models import Q

from apps.geolocalizacion.models import Distrito
from apps.geolocalizacion.forms.forms_distrito import DistritoForm
from apps.usuarios.mixins import ValidatePermissionRequiredMixin

DISTRITO_FIELDS = [
    {'string': 'N°'},
    {'string': 'Distrito'},
    {'string': 'Numero'},
    {'string': 'Localidad'},
    {'string': 'Estado'},
    {'string': 'Acciones'},
]
"""
permission_required = "geolocalizacion.view_distrito"
permission_required = "geolocalizacion.add_distrito"
permission_required = "geolocalizacion.change_distrito"
permission_required = "geolocalizacion.delete_distrito"


#class DistritoListarView(LoginRequiredMixin,TemplateView):

class DistritoListarView(LoginRequiredMixin,ListView):
    login_url = 'usuarios:index'
    model = Distrito
    template_name = "pgcr/apps/geolocalizacion/distrito/listar.html"
    context_object_name = "list_distrito"
"""

class DistritoListarView(LoginRequiredMixin,ValidatePermissionRequiredMixin,TemplateView):
    model = Distrito
    template_name = "geopuntospando/apps/geolocalizacion/distrito/listar.html"
    login_url = 'usuarios:index'

    def get_context_data(self, **kwargs):
        context = super(DistritoListarView, self).get_context_data(**kwargs)
        personatodo = self.model.objects.all()
        personaactiva = self.model.objects.exclude(estado='True')
        context['fields'] = DISTRITO_FIELDS
        context["distrito_count"] = personaactiva
        context["list_distrito"] = personatodo
        return context


class DistritoCrearView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    model = Distrito
    template_name = "pgcr/apps/geolocalizacion/distrito/form.html"
    context_object_name = "obj_distrito"
    form_class = DistritoForm
    success_url = reverse_lazy("geolocalizacion:listar_distrito")
    success_message = "Distrito Creado Exitosamente"

    def form_valid(self, form):
        distrito = form.save(commit=False)
        distrito.uc = self.request.user.id
        distrito.direccion_ip=get_ip(self.request)
        distrito.save()
        return super().form_valid(form)

class DistritoEditarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
    login_url = 'usuarios:index'
    model = Distrito
    template_name = "pgcr/apps/geolocalizacion/distrito/form.html"
    context_object_name = "obj_distrito"
    form_class = DistritoForm
    success_url = reverse_lazy("geolocalizacion:listar_distrito")
    success_message = "Distrito Actualizado Satisfactoriamente"

    def form_valid(self, form):
        distrito = form.save(commit=False)
        distrito.um = self.request.user.id
        distrito.direccion_ip=get_ip(self.request)
        distrito.save()
        return super().form_valid(form)

class DistritoDetalleView(LoginRequiredMixin,DetailView):
    login_url = 'usuarios:index'
    model = Distrito
    template_name = 'pgcr/apps/geolocalizacion/distrito/detalle.html'#url
    context_object_name = 'obj'

class DistritoEliminarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,DeleteView):
    login_url = 'usuarios:index'
    model = Distrito
    template_name= 'pgcr/apps/geolocalizacion/distrito/eliminar.html'
    context_object_name='obj_distrito'
    success_url = reverse_lazy("geolocalizacion:listar_distrito")
    success_message="Distrito Eliminado Exitosamente"

@login_required(login_url='usuarios:index')
def distritodesactivar(request, id):
    distrito = Distrito.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/distrito/estado_desactivar.html'#url

    if not distrito:
        return redirect('geolocalizacion:listar_distrito')

    if request.method=='GET':
        contexto={'obj':distrito}

    if request.method=='POST':
        distrito.estado=False
        distrito.um = request.user.id
        distrito.save()
        messages.error(request, "Distrito Desactivado")
        return redirect('geolocalizacion:listar_distrito')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def distritoactivar(request, id):
    distrito = Distrito.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/distrito/estado_activar.html'#url

    if not distrito:
        return redirect('geolocalizacion:listar_distrito')

    if request.method=='GET':
        contexto={'obj':distrito}

    if request.method=='POST':
        distrito.estado=True
        distrito.um = request.user.id
        distrito.save()
        messages.success(request, "Distrito Activado")
        return redirect('geolocalizacion:listar_distrito')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def cambiar_estado_distrito(request, pk):
    distrito = get_object_or_404(Distrito, pk=pk)
    if distrito.estado:
        distrito.estado = False
        messages.error(request, "Distrito Desactivada")
    else:
        distrito.estado = True
        messages.success(request, "Distrito Activada")
    distrito.um = request.user.id
    distrito.save()
    return redirect('geolocalizacion:listar_distrito')
