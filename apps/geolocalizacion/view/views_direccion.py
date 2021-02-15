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

from apps.geolocalizacion.models import Direccion
from apps.geolocalizacion.forms.forms_direccion import DireccionForm
from apps.usuarios.mixins import ValidatePermissionRequiredMixin
"""
permission_required = "geolocalizacion.view_direccion"
permission_required = "geolocalizacion.add_direccion"
permission_required = "geolocalizacion.change_direccion"
permission_required = "geolocalizacion.delete_direccion"
"""

#class DireccionListarView(LoginRequiredMixin,TemplateView):
class DireccionListarView(LoginRequiredMixin,ValidatePermissionRequiredMixin,ListView):
    login_url = 'usuarios:index'
    model = Direccion
    template_name = "pgcr/apps/geolocalizacion/direccion/listar.html"
    context_object_name = "list_direccion"

class DireccionCrearView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    model = Direccion
    template_name = "pgcr/apps/geolocalizacion/direccion/form.html"
    context_object_name = "obj_direccion"
    form_class = DireccionForm
    success_url = reverse_lazy("geolocalizacion:listar_direccion")
    success_message = "Direccion Creado Exitosamente"

    def form_valid(self, form):
        direccion = form.save(commit=False)
        direccion.uc = self.request.user.id
        direccion.direccion_ip=get_ip(self.request)
        direccion.save()
        return super().form_valid(form)

class DireccionEditarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
    login_url = 'usuarios:index'
    model = Direccion
    template_name = "pgcr/apps/geolocalizacion/direccion/form.html"
    context_object_name = "obj_direccion"
    form_class = DireccionForm
    success_url = reverse_lazy("geolocalizacion:listar_direccion")
    success_message = "Direccion Actualizado Satisfactoriamente"

    def form_valid(self, form):
        direccion = form.save(commit=False)
        direccion.um = self.request.user.id
        direccion.direccion_ip=get_ip(self.request)
        direccion.save()
        return super().form_valid(form)

class DireccionDetalleView(LoginRequiredMixin,DetailView):
    login_url = 'usuarios:index'
    model = Direccion
    template_name = 'pgcr/apps/geolocalizacion/direccion/detalle.html'#url
    context_object_name = 'obj'

class DireccionEliminarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,DeleteView):
    login_url = 'usuarios:index'
    model = Direccion
    template_name= 'pgcr/apps/geolocalizacion/direccion/eliminar.html'
    context_object_name='obj_direccion'
    success_url = reverse_lazy("geolocalizacion:listar_direccion")
    success_message="Direccion Eliminado Exitosamente"

@login_required(login_url='usuarios:index')
def direcciondesactivar(request, id):
    direccion = Direccion.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/direccion/estado_desactivar.html'#url

    if not direccion:
        return redirect('geolocalizacion:listar_direccion')

    if request.method=='GET':
        contexto={'obj':direccion}

    if request.method=='POST':
        direccion.estado=False
        direccion.um = request.user.id
        direccion.save()
        messages.error(request, "Direccion Desactivado")
        return redirect('geolocalizacion:listar_direccion')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def direccionactivar(request, id):
    direccion = Direccion.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/direccion/estado_activar.html'#url

    if not direccion:
        return redirect('geolocalizacion:listar_direccion')

    if request.method=='GET':
        contexto={'obj':direccion}

    if request.method=='POST':
        direccion.estado=True
        direccion.um = request.user.id
        direccion.save()
        messages.success(request, "Direccion Activado")
        return redirect('geolocalizacion:listar_direccion')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def cambiar_estado_direccion(request, pk):
    direccion = get_object_or_404(Direccion, pk=pk)
    if direccion.estado:
        direccion.estado = False
        messages.error(request, "Direccion Desactivada")
    else:
        direccion.estado = True
        messages.success(request, "Direccion Activada")
    direccion.um = request.user.id
    direccion.save()
    return redirect('geolocalizacion:listar_direccion')
