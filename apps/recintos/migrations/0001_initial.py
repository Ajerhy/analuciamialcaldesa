# Generated by Django 3.1.6 on 2021-02-14 15:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geolocalizacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sufragio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('direccion_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('tiposugrafio', models.CharField(help_text='Ingrese Tipo Recuento de Voto', max_length=100, null=True, verbose_name='Nombre Tipo Recuento de Voto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recinto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('direccion_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('nombrerecinto', models.CharField(help_text='Ingrese Nombre del Recinto o Unidad Educativa', max_length=100, null=True, verbose_name='Nombre Recinto o Unidad Educativa')),
                ('numerorecinto', models.CharField(help_text='Ingrese Numero del Recinto', max_length=100, null=True, verbose_name='Numero Recinto')),
                ('recintomesa', models.IntegerField(default=0, verbose_name='Recinto en Mesa')),
                ('recintohabilitado', models.IntegerField(default=0, verbose_name='Recinto en Mesa')),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolocalizacion.localidad')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('direccion_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('numeromesa', models.CharField(help_text='Ingrese su Numero de Mesa', max_length=100, null=True, verbose_name='Numero de Mesa')),
                ('mesahabilitado', models.IntegerField(default=0, verbose_name='Recinto en Mesa')),
                ('recinto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recintos.recinto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Conteo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('direccion_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('delegadomesa', models.CharField(help_text='Ingrese su Nombre o C.I', max_length=100, null=True, verbose_name='Delegado de Mesa')),
                ('presidentemesa', models.CharField(help_text='Ingrese su Nombre o C.I', max_length=100, null=True, verbose_name='Presidente de Mesa')),
                ('codigo_conteo', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='codigo_conteo')),
                ('totalpapeletas', models.IntegerField(default=0, verbose_name='Total de Papeletas o Habilitados')),
                ('votovalidos', models.IntegerField(default=0, verbose_name='Votos Validos')),
                ('votonullo', models.IntegerField(default=0, verbose_name='Votos en Nulos')),
                ('votoblanco', models.IntegerField(default=0, verbose_name='Votos en Blancos')),
                ('votopst', models.IntegerField(default=0, help_text='Pando Somos Todos', verbose_name='Votos en PST')),
                ('votopaso', models.IntegerField(default=0, help_text='Poder Amazonico Social', verbose_name='Votos en PASO')),
                ('votopanbol', models.IntegerField(default=0, help_text='Partido de Accion Nacional Boliviano', verbose_name='Votos PAN-BOL')),
                ('votocid', models.IntegerField(default=0, help_text='Comunidad de Integracion Democratica', verbose_name='Votos en Comunidad de Integracion Democratica')),
                ('votomda', models.IntegerField(default=0, help_text='Movimiento Democratica Autonomista', verbose_name='Votos en MDA')),
                ('votomts', models.IntegerField(default=0, help_text='Movimiento Tercer Sistema', verbose_name='Votos en MTS')),
                ('votovida', models.IntegerField(default=0, help_text='Vision Democratica Amazonica', verbose_name='Votos en VIDA')),
                ('votomasipsp', models.IntegerField(default=0, help_text='Movimiento Al Socialismo IPSP', verbose_name='Votos MAS IPSP')),
                ('nropapeletasobrante', models.IntegerField(default=0, verbose_name='Numero Papeleta Sobrante')),
                ('papeletasobreante', models.IntegerField(default=0, verbose_name='Total de Papeletas Sobrante')),
                ('carnetssobrantes', models.IntegerField(default=0, verbose_name='Total de Carnet Sobrante')),
                ('verificacioncipapeleta', models.BooleanField(default=0, verbose_name='C.I. y Papeletas')),
                ('total', models.IntegerField(default=0, verbose_name='Total de Votos')),
                ('mesa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recintos.mesa')),
                ('sufragio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recintos.sufragio')),
                ('ubicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geolocalizacion.ubicacion')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
