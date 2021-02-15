from django.contrib import admin

from .models import Ubicacion
from .models import Distrito
from .models import Barrio
from .models import Direccion

from .models import Departamentos
from .models import Provincias
from .models import Municipios
from .models import Localidad
#from apps.recintos.models import Recinto
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources

admin.site.register(Ubicacion)
admin.site.register(Direccion)
#############################################################
class ProvinciasInline(admin.TabularInline):
    model = Provincias
    extra = 3
    fields = ('nombreprovincias', 'siglaprovincias','estado')
    list = ()

class ImportExportDepartamentosResource(resources.ModelResource):
    class Meta:
        model = Departamentos
        import_id_fields = ('id',)
        fields = ['id', 'nombredepartamentos', 'sigladepartamentos']

class DepartamentosAdmin(ImportExportModelAdmin):
    resource_class = ImportExportDepartamentosResource
    fieldsets = [
        (None, {'fields': ['nombredepartamentos']},),
        (None, {'fields': ['sigladepartamentos']},),
    ]
    inlines = [ProvinciasInline]
    list_display = ('id', 'nombredepartamentos', 'sigladepartamentos', 'estado')
###############################################################
#admin.site.register(Departamentos)
admin.site.register(Departamentos, DepartamentosAdmin)
#############################################################
class MunicipiosInline(admin.TabularInline):
    model = Municipios
    extra = 2
    fields = ('nombremunicipios', 'siglamunicipios','estado')
    list = ()

class ImportExportProvinciasResource(resources.ModelResource):
    class Meta:
        model = Provincias
        import_id_fields = ('nombreprovincias',)
        fields = ['id', 'departamentos', 'nombreprovincias']

class ProvinciasAdmin(ImportExportModelAdmin):
    resource_class = ImportExportProvinciasResource
    fieldsets = [(None, {'fields': ['nombreprovincias']},), ]
    inlines = [MunicipiosInline]
    list_display = ('id', 'departamentos', 'nombreprovincias', 'estado')
#############################################################
#admin.site.register(Provincias)
admin.site.register(Provincias, ProvinciasAdmin)


#############################################################
class LocalidadInline(admin.TabularInline):
    model = Localidad
    extra = 2
    fields = ('nombrelocalidad','estado')
    list = ()

class ImportExportMunicipiosResource(resources.ModelResource):
    class Meta:
        model = Municipios
        import_id_fields = ('nombremunicipios',)
        fields = ['id', 'provincias', 'nombremunicipios']

class MunicipiosAdmin(ImportExportModelAdmin):
    resource_class = ImportExportMunicipiosResource
    fieldsets = [(None, {'fields': ['nombremunicipios']},), ]
    inlines = [LocalidadInline]
    list_display = ('id', 'provincias', 'nombremunicipios', 'estado')
#############################################################
#admin.site.register(Municipios)
admin.site.register(Municipios,MunicipiosAdmin)


#############################################################

class DistritoInline(admin.TabularInline):
    model = Distrito
    extra = 2
    fields = ('numerodistrito', 'nombredistrito','estado')
    list = ()

class ImportExportLocalidadResource(resources.ModelResource):
    class Meta:
        model = Localidad
        import_id_fields = ('nombrelocalidad',)
        fields = ['id', 'municipios', 'nombrelocalidad']

class LocalidadAdmin(ImportExportModelAdmin):
    resource_class = ImportExportLocalidadResource
    fieldsets = [(None, {'fields': ['nombrelocalidad']},), ]
    inlines = [DistritoInline]
    list_display = ('id', 'municipios', 'nombrelocalidad','estado')

#############################################################
#admin.site.register(Localidad)
admin.site.register(Localidad,LocalidadAdmin)

#############################################################

class BarrioInline(admin.TabularInline):
    model = Barrio
    extra = 2
    fields = ('nombrebarrio', 'siglabarrio','estado')
    list = ()

class ImportExportDistritoResource(resources.ModelResource):
    class Meta:
        model = Distrito
        import_id_fields = ('nombredistrito',)
        fields = ['id', 'localidad', 'nombredistrito','numerodistrito']

class DistritoAdmin(ImportExportModelAdmin):
    resource_class = ImportExportDistritoResource
    fieldsets = [(None, {'fields': ['nombredistrito']},), ]
    inlines = [BarrioInline]
    list_display = ('id', 'localidad', 'numerodistrito', 'nombredistrito','estado')

#############################################################
admin.site.register(Distrito,DistritoAdmin)


class ImportExportBarrioResource(resources.ModelResource):
    class Meta:
        model = Barrio
        import_id_fields = ('id',)
        fields = ['id','distrito','nombrebarrio','siglabarrio']

class BarrioAdmin(ImportExportModelAdmin):
    resource_class = ImportExportBarrioResource
    list_display = ('id','distrito','nombrebarrio','siglabarrio')
#############################################################
admin.site.register(Barrio,BarrioAdmin)