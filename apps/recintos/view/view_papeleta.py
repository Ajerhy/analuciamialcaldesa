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
from apps.recintos.models import Mesa

class PapeletaUsuarioCrearView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    permission_required = "recintos.add_conteo"
    model = Conteo
    template_name = "ana/apps/papeleta/formulario.html"
    #context_object_name = "obj"
    form_class = PapeletaForm
    success_url = reverse_lazy("usuarios:dashboard")
    success_message = "Llenado de Papeleta Creado Exitosamente"

    def get_context_data(self, **kwargs):
        context = super(PapeletaUsuarioCrearView, self).get_context_data(**kwargs)
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        context["mesas"] = Mesa.objects.all()
        return context

    def form_valid(self, form):
        conteo = form.save(commit=False)
        conteo.uc = self.request.user.id
        #conteo.incripcion = timezone.now()
        #persona.incripcion = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        conteo.direccion_ip = get_ip(self.request)
        conteo.save()
        return super().form_valid(form)