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
from apps.recintos.models import Mesa,Recinto
from django.db.models import Sum
#from apps.tecnico.forms import ProfesorForm

MESA_FIELDS = [
    {'string': 'N°'},
    {'string': 'Recinto'},
    {'string': 'Numero Mesa'},
    {'string': 'Habilitados'},
    {'string': 'Estado'},
    {'string': 'Acciones'},
]

class MesaListarView(LoginRequiredMixin,TemplateView):
    model = Mesa
    template_name = 'ana/apps/recintos/mesa/listar.html'
    login_url = 'usuarios:index'

    def get_context_data(self, **kwargs):
        context = super(MesaListarView, self).get_context_data(**kwargs)
        mesatodo = self.model.objects.all()
        mesaactiva = self.model.objects.exclude(estado='False')
        #context['mesas'] = self.model.objects.all().aggregate(Sum('numeromesa'))
        context['mesas'] = self.model.objects.all().count()
        mesahabilitados = Mesa.objects.aggregate(Sum('mesahabilitado'))
        context['mesas_habilitados'] = mesahabilitados
        context['fields'] = MESA_FIELDS
        context["mesa_count"] = mesaactiva
        context["listar_mesa"] = mesatodo
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        return context


@login_required(login_url='usuarios:index')
def RecintoMesaView(request, pk):  # barrio_persona_id=pk
    template_name = "ana/apps/recintos/mesa/listar.html"
    mesa = Mesa.objects.filter(recinto=pk)
    #paciente = Paciente.objects.filter(persona__barrio_id=pk)

    return render(request, template_name, {
        'fields': MESA_FIELDS,
        'listar_mesa': mesa,
        'API_KEY': settings.API_KEY_GOOGLE_MAPS
    })
