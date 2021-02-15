from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.geolocalizacion.models import Barrio
from apps.geolocalizacion.api.serializers_distrito import DistritoSerializer

"""
class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__'
"""

class BarrioSerializer(serializers.ModelSerializer):
    distrito = DistritoSerializer(read_only=True)
    class Meta:
        model = Barrio
        fields = ('id','nombrebarrio','distrito','estado')