from django.conf.urls import url, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.candidatos.api.api_view_candidato import (CandidatoListAPIView)
from apps.candidatos.api.api_view_cargo import (CargoListAPIView)

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('candidato/', CandidatoListAPIView.as_view(), name='listar_candidato_api'),

    path('cargo/', CargoListAPIView.as_view(), name='listar_cargo_api'),
]