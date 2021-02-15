from apps.candidatos.api.api_view_candidato import (CandidatoListAPIView)
from django.urls import path, include

from apps.militantes.api.api_view_socio import (SocioListAPIView,SocioDetalleAPIView)

urlpatterns = [
    path('socio/',SocioListAPIView.as_view(),name='listar_socio_api'),

    path('socio/<str:codigo>',SocioDetalleAPIView.as_view(),name='detalle_socio_api'),
]