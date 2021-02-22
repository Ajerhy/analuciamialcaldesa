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
from apps.recintos.models import Conteo
from apps.recintos.forms.form_papeleta import PapeletaForm

CONTEO_FIELDS = [
    {'string': 'N°'},
    {'string': 'Mesa'},
    {'string': 'Nulo'},
    {'string': 'Blanco'},

    {'string': 'CID'},
    {'string': 'MAS IPSP'},
    {'string': 'PAN-BOL'},
    {'string': 'PST'},
    {'string': 'MTS'},
    {'string': 'FPV'},
    {'string': 'PASO'},
    {'string': 'MDA'},



    {'string': 'Estado'},
    {'string': 'Acciones'},
]
"""
permission_required = "tecnico.view_profesor"
permission_required = "tecnico.add_profesor"
permission_required = "tecnico.change_profesor"
permission_required = "tecnico.delete_profesor"
"""

class ConteoListarView(LoginRequiredMixin,TemplateView):
    model = Conteo
    template_name = 'ana/apps/recintos/conteo/listar.html'
    login_url = 'usuarios:index'

    def get_context_data(self, **kwargs):
        context = super(ConteoListarView, self).get_context_data(**kwargs)
        conteotodo = self.model.objects.all()
        conteoactiva = self.model.objects.exclude(estado='False')
        context['fields'] = CONTEO_FIELDS
        context["conteo_count"] = conteoactiva
        context["listar_conteo"] = conteotodo
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        return context

@login_required(login_url='usuarios:index')
def MesaPapeletaView(request, pk):
    template_name = "ana/apps/recintos/conteo/listar.html"
    papeleta = Conteo.objects.filter(mesa=pk)
    #paciente = Paciente.objects.filter(persona__barrio_id=pk)

    return render(request, template_name, {
        'fields': CONTEO_FIELDS,
        'listar_conteo': papeleta,
        'API_KEY': settings.API_KEY_GOOGLE_MAPS
    })

class PapeletaCrearView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    permission_required = "recintos.add_conteo"
    model = Conteo
    template_name = "ana/apps/recintos/conteo/formulario.html"
    #context_object_name = "obj_usuarios"
    form_class = PapeletaForm
    success_url = reverse_lazy("recintos:listar_conteo")
    success_message = "Llenado de Papeleta Creado Exitosamente"

class ConteoDetalleView(LoginRequiredMixin,DetailView):
    model = Conteo
    template_name = "ana/apps/recintos/conteo/detalle.html"
    context_object_name = "obj"
    login_url = 'usuarios:index'