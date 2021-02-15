from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from rest_framework import status

from apps.geolocalizacion.api.serializers_departamentos import DepartamentosSerializer
from apps.geolocalizacion.models import Departamentos
from django.db.models import Q

class DepartamentosListAPIView(APIView):
    # poner autenticacion
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        departamentos = Departamentos.objects.all()
        data = DepartamentosSerializer(departamentos,many=True).data
        return Response(data)