from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class PersonalizadaUserAdmin(UserAdmin):
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'fields': ('usuario', 'password1', 'password2'),
        }),)
    list_display = ('usuario', 'email', 'is_active', 'is_staff')
    # 'password',
    search_fields = ('usuario',)

    ordering = ('usuario',)

    filter_horizontal = ()
    # filter_vertical = ()
admin.site.register(Usuario, PersonalizadaUserAdmin)