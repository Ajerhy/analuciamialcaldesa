from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from rest_framework import status

from apps.geolocalizacion.api.serializers_municipios import MunicipiosSerializer
from apps.geolocalizacion.models import Municipios
from django.db.models import Q

class MunicipiosListAPIView(APIView):
    # poner autenticacion
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        municipio = Municipios.objects.all()
        data = MunicipiosSerializer(municipio,many=True).data
        return Response(data)