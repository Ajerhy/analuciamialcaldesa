from django.contrib import admin
from .models import Recinto
from .models import Mesa
from .models import Sufragio
from .models import Conteo
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources

#############################################################
class MesasInline(admin.TabularInline):
    model = Mesa
    extra = 1
    fields = ('recinto','numeromesa','mesahabilitado','estado')
    list = ()

class ImportExportRecintoResource(resources.ModelResource):
    class Meta:
        model = Recinto
        import_id_fields = ('id',)
        fields = ['id', 'localidad', 'nombrerecinto', 'numerorecinto', 'recintomesa','recintohabilitado']

class RecintosAdmin(ImportExportModelAdmin):
    resource_class = ImportExportRecintoResource
    fieldsets = [(None, {'fields': ['nombrerecinto']},),
                 (None, {'fields': ['numerorecinto']},),
                 (None, {'fields': ['recintomesa']},),
                 (None, {'fields': ['recintohabilitado']},),
                 ]
    inlines = [MesasInline]
    list_display = ('id', 'localidad', 'nombrerecinto', 'numerorecinto', 'recintomesa','recintohabilitado','estado')

admin.site.register(Recinto, RecintosAdmin)
#############################################################
class ImportExportMesaResource(resources.ModelResource):
    class Meta:
        model = Mesa
        import_id_fields = ('id',)
        fields = ['id','recinto','codigomesa','numeromesa','mesahabilitado','estado']

class MesaAdmin(ImportExportModelAdmin):
    resource_class = ImportExportMesaResource
    list_display = ('id','recinto','codigomesa','numeromesa','mesahabilitado','estado')
admin.site.register(Mesa,MesaAdmin)
#############################################################
class ImportExportSufragioResource(resources.ModelResource):
    class Meta:
        model = Sufragio
        import_id_fields = ('id',)
        fields = ['id','tiposugrafio','estado']

class SufragioAdmin(ImportExportModelAdmin):
    resource_class = ImportExportSufragioResource
    list_display = ('id','tiposugrafio','estado')
admin.site.register(Sufragio,SufragioAdmin)
#############################################################
class ImportExportConteoResource(resources.ModelResource):
    class Meta:
        model = Conteo
        import_id_fields = ('id',)
        fields = ['id','totalpapeletas','votonullo', 'votoblanco',
                    'votocid','votomasipsp','votopanbol','votopst','votomts','votofpv','votopaso','votomda',
                    'papeletasobreante','carnetssobrantes',
                    'verificacioncipapeleta',
                    'nropapeletasobrante','marcadopapeleta','cerrarpapeleta','total']

class ConteoAdmin(ImportExportModelAdmin):
    resource_class = ImportExportConteoResource

    list_display = ('id','totalpapeletas','votonullo', 'votoblanco',
                    'votocid','votomasipsp','votopanbol','votopst','votomts','votofpv','votopaso','votomda',
                    'papeletasobreante','carnetssobrantes',
                    'verificacioncipapeleta',
                    'nropapeletasobrante','marcadopapeleta','cerrarpapeleta','total')
admin.site.register(Conteo,ConteoAdmin)