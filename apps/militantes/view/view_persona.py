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

from apps.militantes.models import Persona
from apps.militantes.form.forms_persona import PersonaForm

# Librerias de terceros
from dal import autocomplete

#class PersonaListarView(LoginRequiredMixin,generic.ListView):
class PersonaListarView(LoginRequiredMixin,TemplateView):
    model = Persona
    template_name ="ana/apps/militantes/persona/listar.html"
    #context_object_name = "list_persona"
    #paginate_by = 5
    login_url = 'usuarios:index'

    def get_queryset(self):
        queryset = self.model.objects.all()
        request_post = self.request.POST
        print(request_post,"Persona")
        if request_post:
            if request_post.get('nombre'):
                queryset = queryset.filter(
                    nombrepersona__icontains=request_post.get('nombre'))
            if request_post.get('paterno'):
                queryset = queryset.filter(
                    paternopersona__icontains=request_post.get('paterno'))
            if request_post.get('materno'):
                queryset = queryset.filter(
                    maternopersona__icontains=request_post.get('materno'))
            if request_post.get('ci'):
                queryset = queryset.filter(
                    cipersona__icontains=request_post.get('ci'))
        print(queryset, "Resultado")
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PersonaListarView, self).get_context_data(**kwargs)
        #Liminar Cagar de Lista Registros .order_by('-id')[:250]
        context["list_persona"] = self.get_queryset().order_by('-id')[:250]

        #context["persona_count"] = self.get_queryset().count()
        context["persona_count"] = self.model.objects.exclude(estado='False')

        context["per_page"] = self.request.POST.get('per_page')

        search = False
        if (
                self.request.POST.get('nombre') or
                self.request.POST.get('paterno') or
                self.request.POST.get('materno') or
                self.request.POST.get('ci')
        ):
            search = True
        context["search"] = search

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class PersonaCrearView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Persona
    template_name = "ana/apps/militantes/persona/form.html"
    context_object_name = "obj_persona"
    form_class = PersonaForm
    success_url = reverse_lazy("militantes:listar_persona")
    success_message = "Persona Creada Exitosamente"
    login_url = 'usuarios:index'

    def form_valid(self, form):
        persona = form.save(commit=False)
        persona.uc = self.request.user.id
        persona.direccion_ip=get_ip(self.request)
        persona.save()
        return super().form_valid(form)

class PersonaEditarView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Persona
    template_name = "ana/apps/militantes/persona/form.html"
    form_class = PersonaForm
    context_object_name = "obj_persona"
    success_url = reverse_lazy("militantes:listar_persona")
    success_message = "Persona Modificada Exitosamente"
    login_url = 'usuarios:index'

    def form_valid(self, form):
        persona = form.save(commit=False)
        persona.um = self.request.user.id
        persona.direccion_ip=get_ip(self.request)
        persona.save()
        return super().form_valid(form)

class PersonaEliminarView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    login_url = 'usuarios:index'
    model = Persona
    template_name= 'ana/apps/militantes/persona/eliminar.html'
    context_object_name='obj_persona'
    success_url = reverse_lazy("militantes:listar_persona")
    success_message="Persona Eliminada Exitosamente"

class PersonaDetalleView(LoginRequiredMixin,DetailView):
    login_url = 'usuarios:index'
    model = Persona
    template_name = 'ana/apps/militantes/persona/detalle.html'#url
    context_object_name = 'obj'

@login_required(login_url='usuarios:index')
def cambiar_estado_persona(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    if persona.estado:
        persona.estado = False
        messages.error(request, "Persona Desactivada")
    else:
        persona.estado = True
        messages.success(request, "Persona Activada")
    #persona.um = request.user.id
    #persona.direccion_ip = get_ip(request)
    persona.save()
    return redirect('militantes:listar_persona')

@login_required(login_url='usuarios:index')
def personadesactivar(request, id):
    persona = Persona.objects.filter(pk=id).first()
    contexto={}
    template_name = 'ana/apps/militantes/persona/estado_desactivar.html'#url

    if not persona:
        return redirect('militantes:listar_persona')

    if request.method=='GET':
        contexto={'obj':persona}

    if request.method=='POST':
        persona.estado=False
        persona.save()
        messages.error(request, "Persona Desactivada")
        return redirect('militantes:listar_persona')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def personaactivar(request, id):
    persona = Persona.objects.filter(pk=id).first()
    contexto={}
    template_name = 'ana/apps/militantes/persona/estado_activar.html'#url

    if not persona:
        return redirect('militantes:listar_persona')

    if request.method=='GET':
        contexto={'obj':persona}

    if request.method=='POST':
        persona.estado=True
        persona.save()
        messages.success(request, "Persona Activada")
        return redirect('militantes:listar_persona')

    return render(request,template_name,contexto)


#Persona Autocompletar
class PersonaAutocompletar(autocomplete.Select2QuerySetView):
    """Servicio de auto completado para el modelo PyCountry
    """
    def get_queryset(self):
        queryset = Persona.objects.all()
        if self.q:
            queryset = queryset.filter(cipersona__icontains=self.q)
        return queryset