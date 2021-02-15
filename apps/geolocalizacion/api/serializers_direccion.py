from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.geolocalizacion.models import Direccion
from apps.geolocalizacion.api.serializers_barrio import BarrioSerializer
from apps.geolocalizacion.api.serializers_ubicacion import UbicacionSerializer

"""
class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'
"""

class DireccionSerializer(serializers.ModelSerializer):
    barrio = BarrioSerializer(read_only=True)
    ubicacion = UbicacionSerializer(read_only=True)
    class Meta:
        model = Direccion
        fields = ('id',
                  'numerocasadireccion', 'referenciadireccion',
                  'barrio', 'ubicacion',
                  'estado')
