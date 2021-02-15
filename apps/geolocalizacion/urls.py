from django.urls import include,path
from rest_framework.urlpatterns import format_suffix_patterns

#Ubicacion
from apps.geolocalizacion.view.views_ubicacion import UbicacionListarView,UbicacionCrearView,UbicacionEditarView,UbicacionDetalleView,\
    UbicacionEliminarView,ubicaciondesactivar,ubicacionactivar,cambiar_estado_ubicacion,PuntosUbicacionView
#UbicacionListView,index,
#Mapa
from apps.geolocalizacion.view.views_ubicacion import PoligonoView,CrearPoligonoView,\
    CirculoView,RectanguloView

#Distrito
from apps.geolocalizacion.view.views_distrito import DistritoListarView,DistritoCrearView,DistritoEditarView,DistritoDetalleView,\
    DistritoEliminarView,distritodesactivar,distritoactivar,cambiar_estado_distrito

#Barrio
from apps.geolocalizacion.view.views_barrio import BarrioListarView,BarrioCrearView,BarrioEditarView,BarrioDetalleView,\
    BarrioEliminarView,barriodesactivar,barrioactivar,cambiar_estado_barrio

#Direccion
from apps.geolocalizacion.view.views_direccion import DireccionListarView,DireccionCrearView,DireccionEditarView,DireccionDetalleView,\
    DireccionEliminarView,direcciondesactivar,direccionactivar,cambiar_estado_direccion

#Departamentos
from apps.geolocalizacion.view.views_departamentos import DepartamentoListarView,DepartamentoCrearView,DepartamentoEditarView,DepartamentoDetalleView,\
    DepartamentoEliminarView,departamentodesactivar,departamentoactivar,cambiar_estado_departamento,\
    cargar_departamentos

#Provincias
from apps.geolocalizacion.view.views_provincias import ProvinciaListarView,ProvinciaCrearView,ProvinciaEditarView,ProvinciaDetalleView,\
    ProvinciaEliminarView,provinciadesactivar,provinciaactivar,cambiar_estado_provincia,\
    cargar_provincias

#Municipios
from apps.geolocalizacion.view.views_municipios import MunicipioListarView,MunicipioCrearView,MunicipioEditarView,MunicipioDetalleView,\
    MunicipioEliminarView,municipiodesactivar,municipioactivar,cambiar_estado_municipio,\
    MunicipioDependienteView,\
    cargar_municipios

from apps.geolocalizacion.view.views_localidad import LocalidadListarView,\
    cargar_localidades

app_name = 'geolocalizacion'

urlpatterns = [
    #Ubicacion

    path('listar/ubicacion/', UbicacionListarView.as_view(), name='listar_ubicacion'),
    path('crear/ubicacion/', UbicacionCrearView.as_view(), name='crear_ubicacion'),
    path('editar/<int:pk>/ubicacion/', UbicacionEditarView.as_view(), name='editar_ubicacion'),
    path('detalle/<int:pk>/ubicacion/', UbicacionDetalleView.as_view(), name='detalle_ubicacion'),
    path('eliminar/<int:pk>/ubicacion/', UbicacionEliminarView.as_view(), name='eliminar_ubicacion'),
    #
    path('desactivar/<int:id>/ubicacion/', ubicaciondesactivar, name='desactivar_ubicacion'),
    path('activar/<int:id>/ubicacion/', ubicacionactivar, name='activar_ubicacion'),
    ##rapido
    path('estado/<int:pk>/ubicacion/', cambiar_estado_ubicacion, name='estado_ubicacion'),
    #
    #path('ubicacion/',index.as_view(),name='index'),
    path('puntos/ubicacion/',PuntosUbicacionView.as_view(),name='puntos_ubicacion'),
    #path('guardar/', ubicacion_guardar, name='ubicacionguardar'),
    #

    #path('ubicacion/json/',UbicacionListView.as_view(),name='json_ubicacion'),

    #Mapa
    path('poligono/',PoligonoView.as_view(),name='poligono'),
    path('crear/poligono/',CrearPoligonoView.as_view(),name='crear_poligono'),

    path('circulo/',CirculoView.as_view(),name='circulo'),

    path('rectangulo/',RectanguloView.as_view(),name='rectangulo'),



    #Distrito
    path('listar/distrito/', DistritoListarView.as_view(), name='listar_distrito'),
    path('crear/distrito/', DistritoCrearView.as_view(), name='crear_distrito'),
    path('editar/<int:pk>/distrito/', DistritoEditarView.as_view(), name='editar_distrito'),
    path('detalle/<int:pk>/distrito/', DistritoDetalleView.as_view(), name='detalle_distrito'),
    path('eliminar/<int:pk>/distrito/', DistritoEliminarView.as_view(), name='eliminar_distrito'),
    #
    path('desactivar/<int:id>/distrito/', distritodesactivar, name='desactivar_distrito'),
    path('activar/<int:id>/distrito/', distritoactivar, name='activar_distrito'),
    ##rapido
    path('estado/<int:pk>/distrito/', cambiar_estado_distrito, name='estado_distrito'),
    #

    #Barrio
    path('listar/barrio/', BarrioListarView.as_view(), name='listar_barrio'),
    path('crear/barrio/', BarrioCrearView.as_view(), name='crear_barrio'),
    path('editar/<int:pk>/barrio/', BarrioEditarView.as_view(), name='editar_barrio'),
    path('detalle/<int:pk>/barrio/', BarrioDetalleView.as_view(), name='detalle_barrio'),
    path('eliminar/<int:pk>/barrio/', BarrioEliminarView.as_view(), name='eliminar_barrio'),
    #
    path('desactivar/<int:id>/barrio/', barriodesactivar, name='desactivar_barrio'),
    path('activar/<int:id>/barrio/', barrioactivar, name='activar_barrio'),
    ##rapido
    path('estado/<int:pk>/barrio/', cambiar_estado_barrio, name='estado_barrio'),
    #

    #Direccion
    path('listar/direccion/', DireccionListarView.as_view(), name='listar_direccion'),
    path('crear/direccion/', DireccionCrearView.as_view(), name='crear_direccion'),
    path('editar/<int:pk>/direccion/', DireccionEditarView.as_view(), name='editar_direccion'),
    path('detalle/<int:pk>/direccion/', DireccionDetalleView.as_view(), name='detalle_direccion'),
    path('eliminar/<int:pk>/direccion/', DireccionEliminarView.as_view(), name='eliminar_direccion'),
    #
    path('desactivar/<int:id>/direccion/', direcciondesactivar, name='desactivar_direccion'),
    path('activar/<int:id>/direccion/', direccionactivar, name='activar_direccion'),
    ##rapido
    path('estado/<int:pk>/direccion/', cambiar_estado_direccion, name='estado_direccion'),
    #

    #Departamentos
    path('listar/departamento/', DepartamentoListarView.as_view(), name='listar_departamento'),
    path('crear/departamento/', DepartamentoCrearView.as_view(), name='crear_departamento'),
    path('editar/<int:pk>/departamento/', DepartamentoEditarView.as_view(), name='editar_departamento'),
    path('detalle/<int:pk>/departamento/', DepartamentoDetalleView.as_view(), name='detalle_departamento'),
    path('eliminar/<int:pk>/departamento/', DepartamentoEliminarView.as_view(), name='eliminar_departamento'),
    #
    path('desactivar/<int:id>/departamento/', departamentodesactivar, name='desactivar_departamento'),
    path('activar/<int:id>/departamento/', departamentoactivar, name='activar_departamento'),
    ##rapido
    path('estado/<int:pk>/departamento/', cambiar_estado_departamento, name='estado_departamento'),
    #
    path('cargar/departamento/', cargar_departamentos, name='cargar_departamentos'),


    #Provincias
    path('listar/provincia/', ProvinciaListarView.as_view(), name='listar_provincia'),
    path('crear/provincia/', ProvinciaCrearView.as_view(), name='crear_provincia'),
    path('editar/<int:pk>/provincia/', ProvinciaEditarView.as_view(), name='editar_provincia'),
    path('detalle/<int:pk>/provincia/', ProvinciaDetalleView.as_view(), name='detalle_provincia'),
    path('eliminar/<int:pk>/provincia/', ProvinciaEliminarView.as_view(), name='eliminar_provincia'),
    #
    path('desactivar/<int:id>/provincia/', provinciadesactivar, name='desactivar_provincia'),
    path('activar/<int:id>/provincia/', provinciaactivar, name='activar_provincia'),
    ##rapido
    path('estado/<int:pk>/provincia/', cambiar_estado_provincia, name='estado_provincia'),
    #
    path('cargar/provincia/', cargar_provincias, name='cargar_provincias'),


    #Municipios
    path('listar/municipio/', MunicipioListarView.as_view(), name='listar_municipio'),
    path('crear/municipio/', MunicipioCrearView.as_view(), name='crear_municipio'),
    path('editar/<int:pk>/municipio/', MunicipioEditarView.as_view(), name='editar_municipio'),
    path('detalle/<int:pk>/municipio/', MunicipioDetalleView.as_view(), name='detalle_municipio'),
    path('eliminar/<int:pk>/municipio/', MunicipioEliminarView.as_view(), name='eliminar_municipio'),
    #
    path('desactivar/<int:id>/municipio/', municipiodesactivar, name='desactivar_municipio'),
    path('activar/<int:id>/municipio/', municipioactivar, name='activar_municipio'),
    ##rapido
    path('estado/<int:pk>/municipio/', cambiar_estado_municipio, name='estado_municipio'),
    #
    path('cargar/municipio/', cargar_municipios, name='cargar_municipios'),
    path('select/dependiente/', MunicipioDependienteView.as_view(), name='select_municipio'),

    # Localidades
    path('listar/localidad/', LocalidadListarView.as_view(), name='listar_localidad'),
    #
    path('cargar/localidad/', cargar_localidades, name='cargar_localidades'),
]
