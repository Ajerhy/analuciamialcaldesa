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
#from apps.tecnico.forms import ProfesorForm

CONTEO_FIELDS = [
    {'string': 'N°'},
    {'string': 'Nulo'},
    {'string': 'Blanco'},
    {'string': 'PST'},
    {'string': 'PASO'},
    {'string': 'PAN-BOL'},
    {'string': 'CID'},
    {'string': 'MDS'},
    {'string': 'MTS'},
    {'string': 'VIDA'},
    {'string': 'MAS IPSP'},
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