from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.geolocalizacion.models import Distrito
from apps.geolocalizacion.api.serializers_localidad import LocalidadSerializer

"""
class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distrito
        fields = '__all__'
"""

class DistritoSerializer(serializers.ModelSerializer):
    localidad = LocalidadSerializer(read_only=True)
    class Meta:
        model = Distrito
        fields = ('id','nombredistrito','localidad','estado')