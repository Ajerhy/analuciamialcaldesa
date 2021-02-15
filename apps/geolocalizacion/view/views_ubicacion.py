from django.shortcuts import render
from django.views.generic import (CreateView, UpdateView, DetailView, TemplateView, View, DeleteView,ListView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from django.template import RequestContext
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import json
from apps.usuarios.templatetags.utils import get_ip
from django.db.models import Q
from django.utils.timesince import timesince
from apps.geolocalizacion.models import Ubicacion
from apps.geolocalizacion.forms.forms_ubicacion import UbicacionForm
from apps.usuarios.mixins import ValidatePermissionRequiredMixin
from analuciamialcaldesa import settings

"""
@login_required(login_url='usuario:index')
def index(request):
    form = UbicacionForm()
    ubicaciones = Ubicacion.objects.all()
    context = {
        'form': form,'ubicaciones': ubicaciones}
    return render_to_response('sapb/apps/geolocalizacion/ubicacion/index.html',context,RequestContext(request))


@login_required(login_url='usuario:index')
def index(request):
    template_name = 'sapb/apps/geolocalizacion/ubicacion/index.html'
    return render(request, template_name)

def ubicacion_guardar(request):
    if request.is_ajax():
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            data = getHTML()
            return HttpResponse(json.dumps({'ok': True, 'msg': data}))
        else:
            return HttpResponse(json.dumps({'ok': False, 'msg': 'Debes llenar todos los campos'}))

#metodo para obtener el html que lista los objetos
def getHTML():
    ubicaciones = Ubicacion.objects.all().order_by('created')

    data = '<select id="cars" name="cars" size="10">'
    for ubicacion in ubicaciones:
        data += '<option value="%s">%s %s - hace %s</option>' % (
        ubicacion.id, ubicacion.latitudubicacion, ubicacion.longitudubicacion, timesince(ubicacion.created))
    data += '</select>' \
            '<button type="button" id="deleteUbicacion">Eliminar</button>'
    return data
"""

"""
class index(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    model = Ubicacion
    template_name = "pgcr/apps/geolocalizacion/ubicacion/index.html"
    context_object_name = "obj_ubicacion"
    form_class = UbicacionForm
    success_url = reverse_lazy("geolocalizacion:index")
    success_message = "Ubicacion Creado Exitosamente"

    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        return context

class UbicacionCreateView(CreateView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        try:
            latitude = data.get("latitude")
            longitude = data.get("longitude")
            address = data.get("address")
            place = Ubicacion.objects.create(latitudubicacion=latitude, longitudubicacion=longitude, descripcionubicacion=address)
            context = {
                "object": {
                    "id": place.id,
                    "latitude": place.latitude,
                    "longitude": place.longitude,
                    "address": place.address
                },
                "result": True
            }
        except Exception as e:
            context = {
                "object": None,
                "result": False,
                "error": str(e)
            }
        return JsonResponse(context)

class UbicacionListView(ListView):
    model = Ubicacion
    queryset = Ubicacion.objects.all()
    def get(self, request, *args, **kwargs):
        super(UbicacionListView, self).get(request, *args, **kwargs)
        context = {"ubicaciones": list(self.object_list.values("latitudubicacion", "longitudubicacion"))}
        return JsonResponse(context)

class UbicacionResetView(View):
    def get(self, request, *args, **kwargs):
        try:
            Ubicacion.objects.all().delete()
            result = True
        except Exception as e:
            result = False
        context = {"object_list": [], "result": result}
        return JsonResponse(context)
"""

UBICACION_FIELDS = [
    {'string': 'N°'},
    {'string': 'Latitud'},
    {'string': 'Longitud'},
    {'string': 'Estado'},
    {'string': 'Acciones'},
]

"""
permission_required = "geolocalizacion.view_ubicacion"
permission_required = "geolocalizacion.add_ubicacion"
permission_required = "geolocalizacion.change_ubicacion"
permission_required = "geolocalizacion.delete_ubicacion"
"""

#class UbicacionListarView(LoginRequiredMixin,ListView):
class UbicacionListarView(LoginRequiredMixin,ValidatePermissionRequiredMixin,TemplateView):
    login_url = 'usuarios:index'
    model = Ubicacion
    template_name = "geopuntospando/apps/geolocalizacion/ubicacion/listar.html"

    def get_context_data(self, **kwargs):
        context = super(UbicacionListarView, self).get_context_data(**kwargs)
        context["API_KEY"]= settings.API_KEY_GOOGLE_MAPS
        context['fields'] = UBICACION_FIELDS
        context["list_ubicacion"] = self.model.objects.all()
        context['ubicacion'] = self.model.objects.exclude(estado=True)
        return context

class PuntosUbicacionView(TemplateView):
    template_name = "geopuntospando/apps/geolocalizacion/ubicacion/puntos.html"
    login_url = 'usuarios:index'
    model = Ubicacion

    def get_context_data(self, **kwargs):
        context = super(PuntosUbicacionView, self).get_context_data(**kwargs)
        context["API_KEY"]= settings.API_KEY_GOOGLE_MAPS
        context["list_ubicacion"] = self.model.objects.all()
        context['ubicacion'] = self.model.objects.exclude(estado=True)
        return context


class UbicacionCrearView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
    login_url = 'usuarios:index'
    model = Ubicacion
    template_name = "geopuntospando/apps/geolocalizacion/ubicacion/formulario.html"
    context_object_name = "obj_ubicacion"
    form_class = UbicacionForm
    success_url = reverse_lazy("geolocalizacion:listar_ubicacion")
    success_message = "Ubicacion Creado Exitosamente"

    def get_context_data(self, **kwargs):
        context = super(UbicacionCrearView, self).get_context_data(**kwargs)
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        return context

    def form_valid(self, form):
        ubicacion = form.save(commit=False)
        ubicacion.uc = self.request.user.id
        ubicacion.direccion_ip=get_ip(self.request)
        ubicacion.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print("El formulario no es válido")
        messages.warning(self.request, "Error del Formulario Creacion Ubicacion")
        return CreateView.form_invalid(self, form)

class UbicacionEditarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
    login_url = 'usuarios:index'
    model = Ubicacion
    template_name = "geopuntospando/apps/geolocalizacion/ubicacion/formulario.html"
    context_object_name = "obj_ubicacion"
    form_class = UbicacionForm
    success_url = reverse_lazy("geolocalizacion:listar_ubicacion")
    #success_message = "Ubicacion Actualizado Satisfactoriamente"

    def get_context_data(self, **kwargs):
        context = super(UbicacionEditarView, self).get_context_data(**kwargs)
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        return context

    def form_valid(self, form):
        ubicacion = form.save(commit=False)
        ubicacion.um = self.request.user.id
        ubicacion.direccion_ip=get_ip(self.request)
        ubicacion.save()
        messages.info(self.request, "Ubicacion Actualizado Exitosamente")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("El formulario no es válido")
        messages.warning(self.request, "Error del Formulario Actualizado Ubicacion")
        return UpdateView.form_invalid(self, form)
        #return super().form_invalid(form)

class UbicacionDetalleView(LoginRequiredMixin,DetailView):
    login_url = 'usuarios:index'
    model = Ubicacion
    template_name = 'geopuntospando/apps/geolocalizacion/ubicacion/detalle.html'#url
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super(UbicacionDetalleView, self).get_context_data(**kwargs)
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        return context

class UbicacionEliminarView(SuccessMessageMixin,LoginRequiredMixin,ValidatePermissionRequiredMixin,DeleteView):
    login_url = 'usuarios:index'
    model = Ubicacion
    template_name= 'geopuntospando/apps/geolocalizacion/ubicacion/eliminar.html'
    context_object_name='obj_ubicacion'
    success_url = reverse_lazy("geolocalizacion:listar_ubicacion")
    success_message="Ubicacion Eliminado Exitosamente"

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(UbicacionEliminarView, self).delete(request, *args, **kwargs)

@login_required(login_url='usuarios:index')
def ubicaciondesactivar(request, id):
    ubicacion = Ubicacion.objects.filter(pk=id).first()
    contexto={}
    template_name = 'geopuntospando/apps/geolocalizacion/ubicacion/estado_desactivar.html'#url

    if not ubicacion:
        return redirect('geolocalizacion:listar_ubicacion')

    if request.method=='GET':
        contexto={'obj':ubicacion}

    if request.method=='POST':
        ubicacion.estado=False
        ubicacion.um = request.user.id
        ubicacion.save()
        messages.error(request, "Ubicacion Desactivado")
        return redirect('geolocalizacion:listar_ubicacion')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def ubicacionactivar(request, id):
    ubicacion = Ubicacion.objects.filter(pk=id).first()
    contexto={}
    template_name = 'geopuntospando/apps/geolocalizacion/ubicacion/estado_activar.html'#url

    if not ubicacion:
        return redirect('geolocalizacion:listar_ubicacion')

    if request.method=='GET':
        contexto={'obj':ubicacion}

    if request.method=='POST':
        ubicacion.estado=True
        ubicacion.um = request.user.id
        ubicacion.save()
        messages.success(request, "Ubicacion Activado")
        return redirect('geolocalizacion:listar_ubicacion')

    return render(request,template_name,contexto)

@login_required(login_url='usuarios:index')
def cambiar_estado_ubicacion(request, pk):
    ubicacion = get_object_or_404(Ubicacion, pk=pk)
    if ubicacion.estado:
        ubicacion.estado = False
        messages.error(request, "Ubicacion Desactivada")
    else:
        ubicacion.estado = True
        messages.success(request, "Ubicacion Activada")
    ubicacion.um = request.user.id
    ubicacion.save()
    return redirect('geolocalizacion:listar_ubicacion')













class CrearPoligonoView(TemplateView):
    template_name = "geopuntospando/apps/geolocalizacion/mapa/crear_poligono.html"
    login_url = 'usuarios:index'
    model = Ubicacion

    def get_context_data(self, **kwargs):
        context = super(CrearPoligonoView, self).get_context_data(**kwargs)
        context["API_KEY"]= settings.API_KEY_GOOGLE_MAPS
        context["list_ubicacion"] = self.model.objects.all()
        context['ubicacion'] = self.model.objects.exclude(estado=True)
        return context

class PoligonoView(TemplateView):
    template_name = "geopuntospando/apps/geolocalizacion/mapa/poligono.html"
    login_url = 'usuarios:index'
    model = Ubicacion

    def get_context_data(self, **kwargs):
        context = super(PoligonoView, self).get_context_data(**kwargs)
        context["API_KEY"]= settings.API_KEY_GOOGLE_MAPS
        context["list_ubicacion"] = self.model.objects.all()
        context['ubicacion'] = self.model.objects.exclude(estado=True)
        return context

class CirculoView(TemplateView):
    template_name = "geopuntospando/apps/geolocalizacion/mapa/circulo.html"
    login_url = 'usuarios:index'
    model = Ubicacion

    def get_context_data(self, **kwargs):
        context = super(CirculoView, self).get_context_data(**kwargs)
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        context["list_ubicacion"] = self.model.objects.all()
        context['ubicacion'] = self.model.objects.exclude(estado=True)
        return context

class RectanguloView(TemplateView):
    template_name = "geopuntospando/apps/geolocalizacion/mapa/rectangulo.html"
    login_url = 'usuarios:index'
    model = Ubicacion

    def get_context_data(self, **kwargs):
        context = super(RectanguloView, self).get_context_data(**kwargs)
        context["API_KEY"] = settings.API_KEY_GOOGLE_MAPS
        context["list_ubicacion"] = self.model.objects.all()
        context['ubicacion'] = self.model.objects.exclude(estado=True)
        return context