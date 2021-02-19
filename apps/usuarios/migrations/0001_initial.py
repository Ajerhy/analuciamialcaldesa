# Generated by Django 3.1.6 on 2021-02-19 03:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='descripcion')),
                ('direccion_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('codigopais', models.CharField(max_length=10, verbose_name='Nombres')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('usuario', models.CharField(max_length=15, unique=True, verbose_name='Usuario')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Correo Electronico')),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefono')),
                ('usuario_img', models.ImageField(blank=True, null=True, upload_to='usuario/%Y/%m/%d/', verbose_name='Imagen de Usuario')),
                ('roles', models.CharField(choices=[('1', 'Administrador'), ('2', 'Usuario'), ('3', 'Encargado de Reciento'), ('4', 'Delegado de Mesa'), ('5', 'Resultado')], default='2', max_length=2)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('codigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.codigo')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
                'ordering': ['-is_active'],
            },
        ),
    ]
