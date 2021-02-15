# Generated by Django 3.1.6 on 2021-02-14 15:03

import apps.militantes.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('direccion_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombreinstitucion', models.CharField(help_text='Ingrese su Nombre Institucion', max_length=250, null=True, verbose_name='Nombre Institucion')),
                ('siglainstitucion', models.CharField(blank=True, help_text='Ingrese la Sigla Institucion', max_length=15, null=True, verbose_name='Sigla Institucion')),
                ('nitinstitucion', models.CharField(blank=True, help_text='Ingrese el Nit o Número de Identifican Tributaria', max_length=25, null=True, verbose_name='Nit de Empresa')),
            ],
            options={
                'verbose_name_plural': 'Instituciones',
                'ordering': ['-creacion'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('direccion_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombrepersona', models.CharField(help_text='Ingrese su Nombre', max_length=100, null=True, verbose_name='Nombre')),
                ('paternopersona', models.CharField(blank=True, help_text='Ingrese su Apellido Paterno', max_length=100, null=True, verbose_name='Apellido Paterno')),
                ('maternopersona', models.CharField(blank=True, help_text='Ingrese su Apellido Materno', max_length=100, null=True, verbose_name='Apellido Materno')),
                ('cipersona', models.CharField(help_text='Ingrese su Numero de Cedula de Identidad', max_length=20, null=True, unique=True, verbose_name='Cedula de Identidad')),
                ('generopersona', models.BooleanField(choices=[(True, 'Hombre'), (False, 'Mujer')], default=1, help_text='Ingrese Genero', verbose_name='Genero')),
                ('nacimientopersona', models.DateField(blank=True, help_text='Seleccione su fecha de nacimiento', null=True, verbose_name='Fecha de nacimiento')),
            ],
            options={
                'verbose_name_plural': 'Personas',
                'ordering': ['-creacion'],
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('direccion_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('codigosocio', models.TextField(blank=True, editable=False, null=True)),
                ('codigo_qr', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='codigo_qr')),
                ('tiposocio', models.BooleanField(choices=[(True, 'Persona'), (False, 'Empresa')], default=1, help_text='Ingrese Tipo de Socio', verbose_name='Tipo de Socio')),
                ('impresion', models.IntegerField(blank=True, null=True)),
                ('informacion', models.CharField(blank=True, help_text='Ingrese Informacion', max_length=60, null=True, verbose_name='Informacion')),
                ('persona', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='militantes.persona')),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Socios',
                'ordering': ['-creacion'],
            },
        ),
        migrations.CreateModel(
            name='Votar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('direccion_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('codigovotar', models.CharField(default=apps.militantes.models.ultimo_numero, max_length=80)),
                ('tiposocio', models.BooleanField(choices=[(True, 'Persona'), (False, 'Empresa')], default=1)),
                ('socio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='militantes.socio')),
            ],
            options={
                'verbose_name_plural': 'Votantes',
                'ordering': ['-creacion'],
            },
        ),
    ]
