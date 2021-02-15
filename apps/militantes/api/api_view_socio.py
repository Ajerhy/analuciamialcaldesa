from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect, get_object_or_404
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,Http404)
from rest_framework import status

from apps.militantes.api.serializers_socio import SocioSerializer
from apps.militantes.models import Socio
from django.db.models import Q

class SocioListAPIView(APIView):
    def get(self,request):
        socio = Socio.objects.all()
        data = SocioSerializer(socio,many=True).data
        return Response(data)


class SocioDetalleAPIView(APIView):
    def get(self,request, codigo):
        #socio = get_object_or_404(Socio, Q(codigo_qr=codigo))
        #socio = get_object_or_404(Socio, Q(codigosocio=codigo) & Q(codigo_qr=codigo))
        socio = get_object_or_404(Socio,Q(codigosocio=codigo)|Q(codigo_qr=codigo))
        data = SocioSerializer(socio).data
        return Response(data)