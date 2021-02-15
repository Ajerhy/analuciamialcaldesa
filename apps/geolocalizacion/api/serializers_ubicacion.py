from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.geolocalizacion.models import Ubicacion

"""
class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'
"""

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ('id','latitudubicacion','longitudubicacion','estado')