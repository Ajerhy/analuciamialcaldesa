from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.geolocalizacion.models import Municipios
from apps.geolocalizacion.api.serializers_provincias import ProvinciasSerializer

"""
class MunicipiosSerializer(serializers.ModelSerializer):
    provincias = ProvinciasSerializer(read_only=True)
    class Meta:
        model = Municipios
        fields = '__all__'
"""
class MunicipiosSerializer(serializers.ModelSerializer):
    provincias = ProvinciasSerializer(read_only=True)
    class Meta:
        model = Municipios
        fields = ('id','nombremunicipios','provincias','estado')