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

from apps.geolocalizacion.models import Provincias
from apps.geolocalizacion.forms.forms_provincias import ProvinciasForm
from apps.usuarios.mixins import ValidatePermissionRequiredMixin

PROVINCIA_FIELDS = [
    {'string': 'N°'},
    {'string': 'Provincia'},
    {'string': 'Departamento'},
    {'string': 'Sigla'},
    {'string': 'Estado'},
    {'string': 'Acciones'},
]
"""
permission_required = "geolocalizacion.view_provincias"
permission_required = "geolocalizacion.add_provincias"
permission_required = "geolocalizacion.change_provincias"
permission_required = "geolocalizacion.delete_provincias"

#class ProvinciaListarView(LoginRequiredMixin,TemplateView):

class ProvinciaListarView(LoginRequiredMixin,ListView):
    login_url = 'usuarios:index'
    model = Provincias
    template_name = "pgcr/apps/geolocalizacion/provincia/listar.html"
    context_object_name = "list_provincia"
"""
class ProvinciaListarView(LoginRequiredMixin,ValidatePermissionRequiredMixin,TemplateView):
  model = Provincias
  template_name = "geopuntospando/apps/geolocalizacion/provincia/listar.html"
  login_url = 'usuarios:index'

  def get_context_data(self, **kwargs):
      context = super(ProvinciaListarView, self).get_context_data(**kwargs)
      personatodo = self.model.objects.all()
      personaactiva = self.model.objects.exclude(estado='True')
      context['fields'] = PROVINCIA_FIELDS
      context["provincia_count"] = personaactiva
      context["list_provincia"] = personatodo
      return context


class ProvinciaCrearView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
  login_url = 'usuarios:index'
  model = Provincias
  template_name = "pgcr/apps/geolocalizacion/provincia/form.html"
  context_object_name = "obj_provincia"
  form_class = ProvinciasForm
  success_url = reverse_lazy("geolocalizacion:listar_provincia")
  success_message = "Provincia Creado Exitosamente"

  def form_valid(self, form):
      provincia = form.save(commit=False)
      provincia.uc = self.request.user.id
      provincia.direccion_ip=get_ip(self.request)
      provincia.save()
      return super().form_valid(form)

class ProvinciaEditarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
  login_url = 'usuarios:index'
  model = Provincias
  template_name = "pgcr/apps/geolocalizacion/provincia/form.html"
  context_object_name = "obj_provincia"
  form_class = ProvinciasForm
  success_url = reverse_lazy("geolocalizacion:listar_provincia")
  success_message = "Provincia Actualizado Satisfactoriamente"

  def form_valid(self, form):
      provincia = form.save(commit=False)
      provincia.um = self.request.user.id
      provincia.direccion_ip=get_ip(self.request)
      provincia.save()
      return super().form_valid(form)

class ProvinciaDetalleView(LoginRequiredMixin,DetailView):
  login_url = 'usuarios:index'
  model = Provincias
  template_name = 'pgcr/apps/geolocalizacion/provincia/detalle.html'#url
  context_object_name = 'obj'

class ProvinciaEliminarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,DeleteView):
  login_url = 'usuarios:index'
  model = Provincias
  template_name= 'pgcr/apps/geolocalizacion/provincia/eliminar.html'
  context_object_name='obj_provincia'
  success_url = reverse_lazy("geolocalizacion:listar_provincia")
  success_message="Provincia Eliminado Exitosamente"

@login_required(login_url='usuarios:index')
def provinciadesactivar(request, id):
  provincia = Provincias.objects.filter(pk=id).first()
  contexto={}
  template_name = 'pgcr/apps/geolocalizacion/provincia/estado_desactivar.html'#url

  if not provincia:
      return redirect('geolocalizacion:listar_provincia')

  if request.method=='GET':
      contexto={'obj':provincia}

  if request.method=='POST':
      provincia.estado=False
      provincia.um = request.user.id
      provincia.save()
      messages.error(request, "Provincia Desactivado")
      return redirect('geolocalizacion:listar_provincia')

  return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def provinciaactivar(request, id):
  provincia = Provincias.objects.filter(pk=id).first()
  contexto={}
  template_name = 'pgcr/apps/geolocalizacion/provincia/estado_activar.html'#url

  if not provincia:
      return redirect('geolocalizacion:listar_provincia')

  if request.method=='GET':
      contexto={'obj':provincia}

  if request.method=='POST':
      provincia.estado=True
      provincia.um = request.user.id
      provincia.save()
      messages.success(request, "Provincia Activado")
      return redirect('geolocalizacion:listar_provincia')

  return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def cambiar_estado_provincia(request, pk):
  provincia = get_object_or_404(Provincias, pk=pk)
  if provincia.estado:
      provincia.estado = False
      messages.error(request, "Provincia Desactivada")
  else:
      provincia.estado = True
      messages.success(request, "Provincia Activada")
  provincia.um = request.user.id
  provincia.save()
  return redirect('geolocalizacion:listar_provincia')

def cargar_provincias(request):
  departamentos_id = request.GET.get('departamentos')
  #provincias = Provincias.objects.filter(departamentos_id=departamentos_id).order_by('nombreprovincias')
  provincias = Provincias.objects.exclude(estado='False')
  return render(request,'pgcr/apps/geolocalizacion/provincia/include/cargar_provincia.html',{'provincias':provincias})