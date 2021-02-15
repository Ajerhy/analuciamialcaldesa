from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView)
from rest_framework.response import Response

from apps.candidatos.models import Cargo
from apps.candidatos.api.serializers_cargo import CargoSerializer

class CargoListAPIView(ListAPIView):
	serializer_class = CargoSerializer
	queryset = Cargo.objects.all()
