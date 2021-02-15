from django.db import transaction
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.views.generic import (CreateView, UpdateView, DetailView, ListView,TemplateView, View, DeleteView)
from apps.candidatos.models import Candidato
from apps.candidatos.form.forms_candidato import CandidatoForm

from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q


#class CandidatosListarView(LoginRequiredMixin,generic.ListView):
class CandidatosListarView(LoginRequiredMixin,TemplateView):
    model = Candidato
    template_name = "ana/apps/candidatos/candidato/listar.html"
    #context_object_name = "list_usuario"
    login_url = 'usuarios:index'

    def get_queryset(self):
        queryset = self.model.objects.all()

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
        context = super(CandidatosListarView, self).get_context_data(**kwargs)
        context["list_candidatos"] = self.get_queryset()
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





def cargar_imagen(request):
    if request.method == 'GET':
        return render(request, 'ana/apps/candidatos/candidato/cargar_imagen.html')
    elif request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            new_imagen = Candidato(
                titulo = form.cleaned_data["titulo"],
                frase=form.cleaned_data["frase"],
                imagen = form.cleaned_data["imagen"])
            new_imagen.save()
            #return HttpResponseRedirect('/gallery/upload_image/')
            return redirect('candidatos:listar_candidato')