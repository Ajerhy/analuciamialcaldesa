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

from apps.militantes.models import Institucion
from apps.militantes.form.forms_institucion import InstitucionForm

#class InstitucionListarView(LoginRequiredMixin,generic.ListView):
class InstitucionListarView(LoginRequiredMixin,TemplateView):
    model = Institucion
    template_name = "ana/apps/militantes/institucion/listar.html"
    #context_object_name = "list_institucion"
    login_url = 'usuarios:index'

    # Q(nombreinstitucion__icontains=request_post.get('institucion'))
    # & Q(siglainstitucion__iexact=request_post.get('institucion'))
    # & Q(nitinstitucion__icontains=request_post.get('institucion'))

    def get_queryset(self):
        #queryset = self.model.objects.all().order_by('-id')[:250]
        queryset = self.model.objects.all()

        request_post = self.request.POST
        print(request_post,"Institucion")
        if request_post:
            if request_post.get('institucion'):
                queryset = queryset.filter(nombreinstitucion__icontains=request_post.get('institucion'))
            if request_post.get('sigla'):
                queryset = queryset.filter(siglainstitucion__icontains=request_post.get('sigla'))
            if request_post.get('nit'):
                queryset = queryset.filter(nitinstitucion__icontains=request_post.get('nit'))

        print(queryset, "Resultado")
        return queryset

    def get_context_data(self, **kwargs):
        context = super(InstitucionListarView, self).get_context_data(**kwargs)
        # Liminar Cagar de Lista Registros .order_by('-id')[:250]
        context["list_institucion"] = self.get_queryset().order_by('-id')[:250]
        #context["institucion_count"] = self.get_queryset().count()
        context["institucion_count"] = Institucion.objects.exclude(estado='False')
        context["per_page"] = self.request.POST.get('per_page')

        search = False
        if (
                self.request.POST.get('institucion') or
                self.request.POST.get('sigla') or
                self.request.POST.get('nit')
        ):
            search = True
        context["search"] = search

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class InstitucionCrearView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url = 'usuario:index'
    model = Institucion
    template_name = "ana/apps/militantes/institucion/form.html"
    context_object_name = "obj_institucion"
    form_class = InstitucionForm
    success_url = reverse_lazy("cooperativa:listar_institucion")
    success_message = "Institucion Creado Exitosamente"

    def form_valid(self, form):
        institucion = form.save(commit=False)
        institucion.uc = self.request.user.id
        institucion.direccion_ip=get_ip(self.request)
        institucion.save()
        return super().form_valid(form)

class InstitucionEditarView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Institucion
    template_name = "ana/apps/militantes/institucion/form.html"
    context_object_name = "obj_institucion"
    form_class = InstitucionForm
    success_url = reverse_lazy("cooperativa:listar_institucion")
    success_message = "Institucion Actualizada Satisfactoriamente"

    def form_valid(self, form):
        institucion = form.save(commit=False)
        institucion.um = self.request.user.id
        institucion.direccion_ip=get_ip(self.request)
        institucion.save()
        return super().form_valid(form)

class InstitucionEliminarView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    login_url = 'usuario:index'
    model = Institucion
    template_name= 'ana/apps/militantes/institucion/eliminar.html'
    context_object_name='obj_institucion'
    success_url = reverse_lazy("cooperativa:listar_institucion")
    success_message="Institucion Eliminada Exitosamente"

class InstitucionDetalleView(LoginRequiredMixin,DetailView):
    login_url = 'usuario:index'
    model = Institucion
    template_name = 'ana/apps/militantes/institucion/detalle.html'#url
    context_object_name = 'obj'

@login_required(login_url='usuario:index')
def instituciondesactivar(request, id):
    institucion = Institucion.objects.filter(pk=id).first()
    contexto={}
    template_name = 'juntospando/apps/militantes/institucion/estado_desactivar.html'#url

    if not institucion:
        return redirect('afiliado:listar_institucion')

    if request.method=='GET':
        contexto={'obj':institucion}

    if request.method=='POST':
        institucion.estado=False
        institucion.save()
        messages.error(request, "Institucion Desactivada")
        return redirect('afiliado:listar_institucion')

    return render(request,template_name,contexto)

@login_required(login_url='usuario:index')
def institucionactivar(request, id):
    institucion = Institucion.objects.filter(pk=id).first()
    contexto={}
    template_name = 'ana/apps/militantes/institucion/estado_activar.html'#url

    if not institucion:
        return redirect('afiliado:listar_institucion')

    if request.method=='GET':
        contexto={'obj':institucion}

    if request.method=='POST':
        institucion.estado=True
        institucion.save()
        messages.success(request, "Institucion Activada")
        return redirect('afiliado:listar_institucion')

    return render(request,template_name,contexto)

@login_required(login_url='usuario:index')
def cambiar_estado_institucion(request, pk):
    institucion = get_object_or_404(Institucion, pk=pk)
    if institucion.estado:
        institucion.estado = False
        messages.error(request, "Institucion Desactivada")
    else:
        institucion.estado = True
        messages.success(request, "Institucion Activada")
    institucion.um = request.user.id
    institucion.save()
    return redirect('afiliado:listar_institucion')

