from django.urls import path, include
from apps.geolocalizacion.api.api_view_departamentos import (DepartamentosListAPIView)
from apps.geolocalizacion.api.api_view_provincias import (ProvinciasListAPIView)
from apps.geolocalizacion.api.api_view_municipios import (MunicipiosListAPIView)
from apps.geolocalizacion.api.api_view_localidad import (LocalidadListAPIView)

from apps.geolocalizacion.api.api_view_distrito import (DistritoListAPIView)
from apps.geolocalizacion.api.api_view_barrio import (BarrioListAPIView)
from apps.geolocalizacion.api.api_view_direccion import (DireccionListAPIView)
from apps.geolocalizacion.api.api_view_ubicacion import (UbicacionListAPIView)

from apps.geolocalizacion.api.api_view_provincias import (ProvinciaView)
#from rest_framework import routers
#router = routers.DefaultRouter()  # add this
#router.register(r'provincias', ProvinciaView, 'crud_provincia')

urlpatterns = [
#    path('', include(router.urls)),
    path('ubicacion/', UbicacionListAPIView.as_view(), name='listar_ubicacion_api'),

    path('departamento/', DepartamentosListAPIView.as_view(), name='listar_departamento_api'),

    path('provincia/', ProvinciasListAPIView.as_view(), name='listar_provincia_api'),

    path('municipio/', MunicipiosListAPIView.as_view(), name='listar_municipio_api'),



    path('distrito/', DistritoListAPIView.as_view(), name='listar_distrito_api'),

    path('barrio/', BarrioListAPIView.as_view(), name='listar_barrio_api'),

    path('direccion/', DireccionListAPIView.as_view(), name='listar_direccion_api'),



    path('localidad/', LocalidadListAPIView.as_view(), name='listar_localidad_api'),
]