from django.db import transaction
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from django.shortcuts import render, redirect, get_object_or_404
import json
from django.views.generic import (CreateView, UpdateView, DetailView, ListView,TemplateView, View, DeleteView)
from apps.militantes.models import Votar
#from apps.militantes.form.froms_votar import VotarForm
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q


#class VotarListarView(LoginRequiredMixin,generic.ListView):
class VotarListarView(LoginRequiredMixin,TemplateView):
    model = Votar
    template_name = "ana/apps/militantes/votar/listar.html"
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
        context = super(VotarListarView, self).get_context_data(**kwargs)
        context["list_votar"] = self.get_queryset()
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