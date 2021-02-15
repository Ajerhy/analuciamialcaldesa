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

from apps.geolocalizacion.models import Barrio
from apps.geolocalizacion.forms.forms_barrio import BarrioForm
from apps.usuarios.mixins import ValidatePermissionRequiredMixin

BARRIO_FIELDS = [
    {'string': 'N°'},
    {'string': 'Barrio'},
    {'string': 'Sigla'},
    {'string': 'Distrito'},
    {'string': 'Estado'},
    {'string': 'Acciones'},
]
"""
permission_required = "geolocalizacion.view_barrio"
permission_required = "geolocalizacion.add_barrio"
permission_required = "geolocalizacion.change_barrio"
permission_required = "geolocalizacion.delete_barrio"


#class BarrioListarView(LoginRequiredMixin,TemplateView):
class BarrioListarView(LoginRequiredMixin,ListView):
    login_url = 'usuarios:index'
    model = Barrio
    template_name = "pgcr/apps/geolocalizacion/barrio/listar.html"
    context_object_name = "list_barrio"
"""

class BarrioListarView(LoginRequiredMixin,ValidatePermissionRequiredMixin,TemplateView):
    model = Barrio
    template_name = "geopuntospando/apps/geolocalizacion/barrio/listar.html"
    login_url = 'usuarios:index'

    def get_context_data(self, **kwargs):
        context = super(BarrioListarView, self).get_context_data(**kwargs)
        personatodo = self.model.objects.all()
        personaactiva = self.model.objects.exclude(estado='True')
        context['fields'] = BARRIO_FIELDS
        context["barrio_count"] = personaactiva
        context["list_barrio"] = personatodo
        return context





class BarrioCrearView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    model = Barrio
    template_name = "pgcr/apps/geolocalizacion/barrio/form.html"
    context_object_name = "obj_barrio"
    form_class = BarrioForm
    success_url = reverse_lazy("geolocalizacion:listar_barrio")
    success_message = "Barrio Creado Exitosamente"

    def form_valid(self, form):
        barrio = form.save(commit=False)
        barrio.uc = self.request.user.id
        barrio.direccion_ip=get_ip(self.request)
        barrio.save()
        return super().form_valid(form)

class BarrioEditarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
    login_url = 'usuarios:index'
    model = Barrio
    template_name = "pgcr/apps/geolocalizacion/barrio/form.html"
    context_object_name = "obj_barrio"
    form_class = BarrioForm
    success_url = reverse_lazy("geolocalizacion:listar_barrio")
    success_message = "Barrio Actualizado Satisfactoriamente"

    def form_valid(self, form):
        barrio = form.save(commit=False)
        barrio.um = self.request.user.id
        barrio.direccion_ip=get_ip(self.request)
        barrio.save()
        return super().form_valid(form)

class BarrioDetalleView(LoginRequiredMixin,DetailView):
    login_url = 'usuarios:index'
    model = Barrio
    template_name = 'pgcr/apps/geolocalizacion/barrio/detalle.html'#url
    context_object_name = 'obj'

class BarrioEliminarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,DeleteView):
    login_url = 'usuarios:index'
    model = Barrio
    template_name= 'pgcr/apps/geolocalizacion/barrio/eliminar.html'
    context_object_name='obj_barrio'
    success_url = reverse_lazy("geolocalizacion:listar_barrio")
    success_message="Barrio Eliminado Exitosamente"

@login_required(login_url='usuarios:index')
def barriodesactivar(request, id):
    barrio = Barrio.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/barrio/estado_desactivar.html'#url

    if not barrio:
        return redirect('geolocalizacion:listar_barrio')

    if request.method=='GET':
        contexto={'obj':barrio}

    if request.method=='POST':
        barrio.estado=False
        barrio.um = request.user.id
        barrio.save()
        messages.error(request, "Barrio Desactivado")
        return redirect('geolocalizacion:listar_barrio')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def barrioactivar(request, id):
    barrio = Barrio.objects.filter(pk=id).first()
    contexto={}
    template_name = 'pgcr/apps/geolocalizacion/barrio/estado_activar.html'#url

    if not barrio:
        return redirect('geolocalizacion:listar_barrio')

    if request.method=='GET':
        contexto={'obj':barrio}

    if request.method=='POST':
        barrio.estado=True
        barrio.um = request.user.id
        barrio.save()
        messages.success(request, "Barrio Activado")
        return redirect('geolocalizacion:listar_barrio')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def cambiar_estado_barrio(request, pk):
    barrio = get_object_or_404(Barrio, pk=pk)
    if barrio.estado:
        barrio.estado = False
        messages.error(request, "Barrio Desactivada")
    else:
        barrio.estado = True
        messages.success(request, "Barrio Activada")
    barrio.um = request.user.id
    barrio.save()
    return redirect('geolocalizacion:listar_barrio')
