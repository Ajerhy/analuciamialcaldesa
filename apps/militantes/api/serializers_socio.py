from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.militantes.models import Socio

class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socio
        fields = '__all__'

from rest_framework import serializers
