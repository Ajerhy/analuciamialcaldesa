from django.urls import path
from django.urls import include, re_path
from apps.recintos.view.view_conteo import ConteoListarView
from apps.recintos.view.view_recinto import RecintoListarView
from apps.recintos.view.view_mesa import MesaListarView

app_name = 'recintos'

urlpatterns = [
    path('listar/conteo/', ConteoListarView.as_view(), name='listar_conteo'),

    path('listar/recinto/', RecintoListarView.as_view(), name='listar_recinto'),

    path('listar/mesa/', MesaListarView.as_view(), name='listar_mesa'),
    #path('crear/persona/', PersonaCrearView.as_view(), name='crear_conteo'),
]