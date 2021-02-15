from django.urls import path
#Cargos
from apps.candidatos.view.view_cargo import CargosListarView

#Candidatos
from apps.candidatos.view.view_candidato import CandidatosListarView,\
    cargar_imagen

app_name = 'candidatos'

urlpatterns = [
    # Cargos
    path('listar/cargo/', CargosListarView.as_view(), name='listar_cargo'),

    # Candidatos
    path('listar/candidato/', CandidatosListarView.as_view(), name='listar_candidato'),

    path('crear/candidato/imagen/', cargar_imagen, name='cargar_imagen'),


]