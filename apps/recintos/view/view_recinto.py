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
from apps.recintos.models import Recinto
from django.db.models import Sum
#from apps.tecnico.forms import ProfesorForm

CONTEO_FIELDS = [
    {'string': 'N°'},
    {'string': 'Localidad'},
    {'string': 'Nombre'},
    {'string': 'Sigla'},
    {'string': 'Mesas'},
    {'string': 'Habilitado'},
    {'string': 'Estado'},
    {'string': 'Acciones'},
]

class RecintoListarView(LoginRequiredMixin,TemplateView):
    model = Recinto
    template_name = 'ana/apps/recintos/recinto/listar.html'
    login_url = 'usuarios:index'

    def get_context_data(self, **kwargs):
        context = super(RecintoListarView, self).get_context_data(**kwargs)
        recintotodo = self.model.objects.all()
        recintoactiva = self.model.objects.exclude(estado='False')
        context['recintos_habilitados'] = self.model.objects.aggregate(Sum('recintomesa'))
        context['votacion_habilitados'] = self.model.objects.aggregate(Sum('recintohabilitado'))

        context['recintos'] = self.model.objects.all().count()
        context['fields'] = CONTEO_FIELDS
        context["recinto_count"] = recintoactiva
        context["listar_recinto"] = recintotodo
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        return context

class RecintoDetalleView(LoginRequiredMixin,DetailView):
    model = Recinto
    template_name = "ana/apps/recintos/recinto/detalle.html"
    context_object_name = "obj"
    login_url = 'usuarios:index'