from django.db import transaction
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.views.generic import (CreateView, UpdateView, DetailView, ListView,TemplateView, View, DeleteView)
from apps.militantes.models import Socio
from apps.militantes.form.forms_socio import SocioForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q


#class SocioListarView(LoginRequiredMixin,generic.ListView):

"""
class SocioListarView(LoginRequiredMixin,TemplateView):
    model = Socio
    template_name = "juntospando/apps/militantes/socio/listar.html"
    #context_object_name = "list_usuario"
    login_url = 'usuarios:index'

    def get_queryset(self):
        #queryset = self.model.objects.all()
        queryset = self.model.objects.exclude(usuario__is_superuser=True)

        request_post = self.request.POST
        print(request_post,"Usuario")
        if request_post:
            if request_post.get('usuario'):
                queryset = queryset.filter(
                    usuario__icontains=request_post.get('usuario'))
            if request_post.get('email'):
                queryset = queryset.filter(
                    email__icontains=request_post.get('email'))
        print(queryset, "Resultado")
        return queryset

    def get_context_data(self, **kwargs):
        context = super(SocioListarView, self).get_context_data(**kwargs)
        context["list_socio"] = self.get_queryset()
        context["per_page"] = self.request.POST.get('per_page')

        search = False
        if (
                self.request.POST.get('usuario') or
                self.request.POST.get('email')
        ):
            search = True
        context["search"] = search

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
"""


class SocioListarView(LoginRequiredMixin,ListView):
    login_url = 'usuarios:index'
    model = Socio
    template_name = "ana/apps/militantes/socio/listar.html"
    context_object_name = "list_socio"

#Socio Crear
class SocioCrearView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = Socio
    template_name = "ana/apps/militantes/socio/form.html"
    context_object_name = "obj"
    form_class = SocioForm
    success_url = reverse_lazy("militantes:listar_socio")
    success_message = "Socio Creado Exitosamente"
    login_url = 'usuarios:index'

#Socio Editar
class SocioEditaView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model = Socio
    template_name = "ana/apps/militantes/socio/form.html"
    context_object_name = "obj"
    form_class = SocioForm
    success_url = reverse_lazy("militantes:listar_socio")
    success_message = "Socio Actualizada Satisfactoriamente"
    login_url = 'usuarios:index'

#Socio Detalle
class SocioDetalleView(LoginRequiredMixin,DetailView):
    model = Socio
    template_name = "ana/apps/militantes/socio/detalle.html"
    context_object_name = "obj"
    login_url = 'usuarios:index'

#Eliminar
class SocioEliminarView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Socio
    template_name= "ana/apps/militantes/socio/eliminar.html"
    context_object_name='obj_perfil'
    success_url = reverse_lazy("militantes:listar_socio")
    success_message="Socio Eliminada Exitosamente"
    login_url = 'usuarios:index'



"""
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

"""