from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response

from apps.candidatos.models import Candidato
from apps.candidatos.api.serializers_candidato import CandidatoSerializer

class CandidatoListAPIView(ListAPIView):
	serializer_class = CandidatoSerializer
	queryset = Candidato.objects.all()