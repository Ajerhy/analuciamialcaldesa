from django.urls import path

from apps.militantes.view.view_institucion import InstitucionListarView
from apps.militantes.view.view_persona import PersonaListarView
from apps.militantes.view.view_socio import SocioListarView,\
    SocioCrearView,SocioEditaView,SocioDetalleView,SocioEliminarView
from apps.militantes.view.view_votar import VotarListarView

app_name = 'militantes'

urlpatterns = [
    path('listar/institucion', InstitucionListarView.as_view(), name='listar_institucion'),

    path('listar/persona', PersonaListarView.as_view(), name='listar_persona'),

    #Socio
    path('listar/socio', SocioListarView.as_view(), name='listar_socio'),
    path('crear/socio', SocioCrearView.as_view(), name='crear_socio'),
    path('editar/<int:pk>/socio/', SocioEditaView.as_view(), name='editar_socio'),
    path('detalle/<int:pk>/socio/', SocioDetalleView.as_view(), name='detalle_socio'),
    path('eliminar/<int:pk>/socio/', SocioEliminarView.as_view(), name='eliminar_socio'),

    #Votar
    path('votar/listar', VotarListarView.as_view(), name='listar_votar'),
]