from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario,Codigo
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export.widgets import ManyToManyWidget

class ImportExportUsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario
        import_id_fields = ('id',)
        fields = ['id','usuario','email','last_login','date_joined',
                  'roles','is_active','is_superuser', 'is_staff','password','nombre','apellido','telefono','codigo']

class PersonalizadaUserAdmin(UserAdmin,ImportExportModelAdmin):
    resource_class = ImportExportUsuarioResource

    add_fieldsets = (
        (None, {
            'fields': ('usuario', 'password1', 'password2'),
        }),)
    list_display = ('usuario', 'email', 'is_active', 'is_staff')
    # 'password',
    search_fields = ('usuario',)
    ordering = ('usuario',)
    filter_horizontal = ()
    fieldsets = (
        ('Usuario', {'fields': ('usuario', 'password')}),
        ('Persona Informacion', {'fields': ('nombre',
                                            'apellido',
                                            'email',
                                            'codigo',
                                            'telefono',
                                            'roles',
                                            'usuario_img',
                                            'observaciones'
                                            )}),
        ('Permissions', {'fields': ('is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',
                                    'user_permissions')}),
    )

    # filter_vertical = ()
admin.site.register(Usuario, PersonalizadaUserAdmin)

class ImportExportCodigoResource(resources.ModelResource):
    class Meta:
        model = Codigo
        import_id_fields = ('id',)
        fields = ['id','codigopais','estado']

class CodigoAdmin(ImportExportModelAdmin):
    resource_class = ImportExportCodigoResource
    list_display = ('id','codigopais','estado')
admin.site.register(Codigo,CodigoAdmin)