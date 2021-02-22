from apps.usuarios.forms.form_login import LoginForm
from django.views.generic import (TemplateView, View)
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from analuciamialcaldesa import settings
from django.contrib.auth.models import Group
from apps.usuarios.models import Usuario
from apps.recintos.models import Recinto,Conteo,Mesa
from django.db.models import Sum
# Login

class SinPrivilegios(LoginRequiredMixin,PermissionRequiredMixin):
    login_url = 'usuarios:index'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='usuarios:sinprivilegio'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class DashboardSinPrivilegio(LoginRequiredMixin, TemplateView):
    login_url = 'usuarios:index'
    template_name="ana/apps/usuarios/permiso/privilegio.html"

class LoginView(TemplateView,LoginRequiredMixin):
    login_url = "usuarios:index"
    template_name = "ana/apps/index.html"
    success_url = reverse_lazy("usuarios:dashboard")#url

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST, request=request)
        if form.is_valid():
            user = Usuario.objects.filter(usuario=request.POST.get('usuario')).first()
            if user is not None:
                if user.is_active:
                    user = authenticate(
                        usuario=request.POST.get('usuario'),
                        password=request.POST.get('password'))
                    if user is not None:
                        login_django(request, user)
                        return redirect('usuarios:dashboard')
                    return render(request, self.template_name, {
                        "error": True,
                        "message": "Tu nombre de usuario y contraseña no coinciden. Inténtalo de nuevo."}
                                  )
                return render(request, self.template_name, {
                    "error": True,
                    "message": "Su cuenta está inactiva. Por favor, póngase en contacto con el administrador"}
                              )
            return render(request, self.template_name, {
                "error": True,
                "message": "Tu cuenta no se encuentra. Por favor, póngase en contacto con el administrador"}
                          )
        return render(request, self.template_name, {
            # "error": True,
            # "message": "Tu nombre de Usuario y Contraseña no coinciden. Inténtalo de nuevo."
            "form": form
        })

@login_required(login_url='usuarios:index')
def LogoutView(request):
    logout_django(request)
    return redirect('usuarios:index')

class DashboarView(LoginRequiredMixin,TemplateView):
    login_url = 'usuarios:index'
    template_name = "ana/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboarView, self).get_context_data(**kwargs)
        #= self.model.objects.exclude(is_superuser=True)
        #context["usuarios"] = self.model.objects(is_active=True)
        usuarios = Usuario.objects.filter(is_active=True)

        recintos = Recinto.objects.all()
        sumarecintos = Recinto.objects.aggregate(Sum('recintomesa'))
        sumahabilitados = Recinto.objects.aggregate(Sum('recintohabilitado'))


        context["usuarios"] = usuarios
        context["mesas"] = sumarecintos
        context["habilitados"] = sumahabilitados
        context["recintos_count"] = recintos.count()
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        return context

class ResultadoView(LoginRequiredMixin,TemplateView):
    login_url = 'usuarios:index'
    template_name = "ana/estadistica/resultado.html"

class LineaView(LoginRequiredMixin,TemplateView):
    login_url = 'usuarios:index'
    template_name = "ana/estadistica/linea.html"

    def get_context_data(self, **kwargs):
        context = super(LineaView, self).get_context_data(**kwargs)

        context['mesas_habilitados'] = Mesa.objects.aggregate(Sum('mesahabilitado'))
        context["nulos"] = Conteo.objects.aggregate(Sum('votonullo'))
        context["blancos"] = Conteo.objects.aggregate(Sum('votoblanco'))
        context["cid"] = Conteo.objects.aggregate(Sum('votocid'))
        context["masipsp"] = Conteo.objects.aggregate(Sum('votomasipsp'))
        context["panbol"] = Conteo.objects.aggregate(Sum('votopanbol'))
        context["pst"] = Conteo.objects.aggregate(Sum('votopst'))
        context["mts"] = Conteo.objects.aggregate(Sum('votomts'))
        context["fpv"] = Conteo.objects.aggregate(Sum('votofpv'))
        context["paso"] = Conteo.objects.aggregate(Sum('votopaso'))
        context["mda"] = Conteo.objects.aggregate(Sum('votomda'))
        context["total_papeleta"] = Conteo.objects.aggregate(Sum('marcadopapeleta'))
        context["total"] = Conteo.objects.aggregate(Sum('total'))
        return context




class BarraView(LoginRequiredMixin,TemplateView):
    login_url = 'usuarios:index'
    template_name = "ana/estadistica/barra.html"

    def get_context_data(self, **kwargs):
        context = super(BarraView, self).get_context_data(**kwargs)
        context['mesas_habilitados'] = Mesa.objects.aggregate(Sum('mesahabilitado'))
        context["nulos"] = Conteo.objects.aggregate(Sum('votonullo'))
        context["blancos"] = Conteo.objects.aggregate(Sum('votoblanco'))
        context["cid"] = Conteo.objects.aggregate(Sum('votocid'))
        context["masipsp"] = Conteo.objects.aggregate(Sum('votomasipsp'))
        context["panbol"] = Conteo.objects.aggregate(Sum('votopanbol'))
        context["pst"] = Conteo.objects.aggregate(Sum('votopst'))
        context["mts"] = Conteo.objects.aggregate(Sum('votomts'))
        context["fpv"] = Conteo.objects.aggregate(Sum('votofpv'))
        context["paso"] = Conteo.objects.aggregate(Sum('votopaso'))
        context["mda"] = Conteo.objects.aggregate(Sum('votomda'))
        context["total_papeleta"] = Conteo.objects.aggregate(Sum('marcadopapeleta'))
        context["total"] = Conteo.objects.aggregate(Sum('total'))
        return context

class GrupoCambioUsuario(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            request.session['group'] = Group.objects.get(pk=self.kwargs['pk'])
        except:
            pass
        return HttpResponseRedirect(reverse_lazy("usuarios:dashboard"))


class PapeletaView(LoginRequiredMixin,TemplateView):
    login_url = 'usuarios:index'
    template_name = "ana/apps/papeleta/papeleta.html"