from django.urls import path
from django.urls import include, re_path
from apps.recintos.view.view_conteo import ConteoListarView,MesaPapeletaView,PapeletaCrearView
from apps.recintos.view.view_recinto import RecintoListarView
from apps.recintos.view.view_mesa import MesaListarView,RecintoMesaView

app_name = 'recintos'

urlpatterns = [
    path('listar/papeleta/', ConteoListarView.as_view(), name='listar_conteo'),
    path('papeleta/crear/', PapeletaCrearView.as_view(), name='crear_papeleta'),

    path('listar/recinto/', RecintoListarView.as_view(), name='listar_recinto'),

    path('listar/mesa/', MesaListarView.as_view(), name='listar_mesa'),
    #path('crear/persona/', PersonaCrearView.as_view(), name='crear_conteo'),

    path('recinto/mesa/<int:pk>/ver/', RecintoMesaView, name='mesa_recinto'),

    path('mesa/papeleta/<int:pk>/ver/', MesaPapeletaView, name='papeleta_mesa'),
]