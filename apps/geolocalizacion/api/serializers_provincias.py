from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.geolocalizacion.models import Provincias
from apps.geolocalizacion.api.serializers_departamentos import DepartamentosSerializer

"""
class ProvinciasSerializer(serializers.ModelSerializer):
    departamentos = DepartamentosSerializer(read_only=True)
    class Meta:
        model = Provincias
        fields = '__all__'
"""
class ProvinciasSerializer(serializers.ModelSerializer):
    departamentos = DepartamentosSerializer(read_only=True)
    class Meta:
        model = Provincias
        fields = ('id','nombreprovincias','departamentos','estado')