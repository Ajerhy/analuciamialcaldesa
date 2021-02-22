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

class PapeletaUsuarioCrearView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    permission_required = "recintos.add_conteo"
    model = Conteo
    template_name = "ana/apps/papeleta/formulario.html"
    #context_object_name = "obj"
    form_class = PapeletaForm
    success_url = reverse_lazy("usuarios:dashboard")
    success_message = "Llenado de Papeleta Creado Exitosamente"