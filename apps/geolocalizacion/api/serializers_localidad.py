from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.geolocalizacion.models import Localidad
from apps.geolocalizacion.api.serializers_municipios import MunicipiosSerializer

"""
class LocalidadSerializer(serializers.ModelSerializer):
    municipios = MunicipiosSerializer(read_only=True)
    class Meta:
        model = Localidad
        fields = '__all__'
"""
class LocalidadSerializer(serializers.ModelSerializer):
    municipios = MunicipiosSerializer(read_only=True)
    class Meta:
        model = Localidad
        fields = ('id','nombrelocalidad','municipios','estado')