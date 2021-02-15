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

from apps.geolocalizacion.models import Departamentos
from apps.geolocalizacion.forms.forms_departamentos import DepartamentosForm
from apps.usuarios.mixins import ValidatePermissionRequiredMixin

DEPARTAMENTO_FIELDS = [
    {'string': 'N°'},
    {'string': 'Departamento'},
    {'string': 'Sigla'},
    {'string': 'Estado'},
    {'string': 'Acciones'},
]
"""
permission_required = "geolocalizacion.view_departamentos"
permission_required = "geolocalizacion.add_departamentos"
permission_required = "geolocalizacion.change_departamentos"
permission_required = "geolocalizacion.delete_departamentos"

#class DepartamentoListarView(LoginRequiredMixin,TemplateView):

class DepartamentoListarView(LoginRequiredMixin,ListView):
    login_url = 'usuarios:index'
    model = Departamentos
    template_name = "pgcr/apps/geolocalizacion/departamento/listar.html"
    context_object_name = "list_departamento"
"""

class DepartamentoListarView(LoginRequiredMixin,ValidatePermissionRequiredMixin,TemplateView):
    model = Departamentos
    template_name = "geopuntospando/apps/geolocalizacion/departamento/listar.html"
    login_url = 'usuarios:index'

    def get_context_data(self, **kwargs):
        context = super(DepartamentoListarView, self).get_context_data(**kwargs)
        personatodo = self.model.objects.all()
        personaactiva = self.model.objects.exclude(estado='True')
        context['fields'] = DEPARTAMENTO_FIELDS
        context["departamento_count"] = personaactiva
        context["list_departamento"] = personatodo
        return context



class DepartamentoCrearView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    model = Departamentos
    template_name = "pgcr/apps/geolocalizacion/departamento/form.html"
    context_object_name = "obj_departamento"
    form_class = DepartamentosForm
    success_url = reverse_lazy("geolocalizacion:listar_departamento")
    success_message = "Departamento Creado Exitosamente"

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.uc = self.request.user.id
        departamento.direccion_ip=get_ip(self.request)
        departamento.save()
        return super().form_valid(form)

class DepartamentoEditarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
    login_url = 'usuarios:index'
    model = Departamentos
    template_name = "pgcr/apps/geolocalizacion/departamento/form.html"
    context_object_name = "obj_departamento"
    form_class = DepartamentosForm
    success_url = reverse_lazy("geolocalizacion:listar_departamento")
    success_message = "Departamento Actualizado Satisfactoriamente"

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.um = self.request.user.id
        departamento.direccion_ip=get_ip(self.request)
        departamento.save()
        return super().form_valid(form)

class DepartamentoDetalleView(LoginRequiredMixin,DetailView):
    login_url = 'usuarios:index'
    model = Departamentos
    template_name = 'pgcr/apps/geolocalizacion/departamento/detalle.html'#url
    context_object_name = 'obj'

class DepartamentoEliminarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,DeleteView):
    login_url = 'usuarios:index'
    model = Departamentos
    template_name= 'pgcr/apps/geolocalizacion/departamento/eliminar.html'
    context_object_name='obj_departamento'
    success_url = reverse_lazy("geolocalizacion:listar_departamento")
    success_message="Departamento Eliminado Exitosamente"

@login_required(login_url='usuarios:index')
def departamentodesactivar(request, id):
    departamento = Departamentos.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/departamento/estado_desactivar.html'#url

    if not departamento:
        return redirect('geolocalizacion:listar_departamento')

    if request.method=='GET':
        contexto={'obj':departamento}

    if request.method=='POST':
        departamento.estado=False
        departamento.um = request.user.id
        departamento.save()
        messages.error(request, "Departamento Desactivado")
        return redirect('geolocalizacion:listar_departamento')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def departamentoactivar(request, id):
    departamento = Departamentos.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/departamento/estado_activar.html'#url

    if not departamento:
        return redirect('geolocalizacion:listar_departamento')

    if request.method=='GET':
        contexto={'obj':departamento}

    if request.method=='POST':
        departamento.estado=True
        departamento.um = request.user.id
        departamento.save()
        messages.success(request, "Departamento Activado")
        return redirect('geolocalizacion:listar_departamento')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def cambiar_estado_departamento(request, pk):
    departamento = get_object_or_404(Departamentos, pk=pk)
    if departamento.estado:
        departamento.estado = False
        messages.error(request, "Departamento Desactivada")
    else:
        departamento.estado = True
        messages.success(request, "Departamento Activada")
    departamento.um = request.user.id
    departamento.save()
    return redirect('geolocalizacion:listar_departamento')

def cargar_departamentos(request):
    departamentos = Departamentos.objects.filter().order_by('nombredepartamentos')
    #departamentos = Departamentos.objects.exclude(estado='False')
    return render(request,'pgcr/apps/geolocalizacion/departamento/include/cargar_departamento.html',{'departamentos':departamentos})