from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from rest_framework import status

from apps.geolocalizacion.api.serializers_provincias import ProvinciasSerializer
from apps.geolocalizacion.models import Provincias
from django.db.models import Q

class ProvinciasListAPIView(APIView):
    # poner autenticacion
    #permission_classes = (IsAuthenticated,)
    def get(self,request):
        provincias = Provincias.objects.all()
        data = ProvinciasSerializer(provincias,many=True).data
        return Response(data)

from rest_framework import viewsets

class ProvinciaView(viewsets.ModelViewSet):       # add this
  serializer_class = ProvinciasSerializer          # add this
  queryset = Provincias.objects.all()