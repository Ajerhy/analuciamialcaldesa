# Generated by Django 3.1.6 on 2021-02-26 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recintos', '0002_auto_20210222_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conteo',
            name='certificado_img',
        ),
        migrations.AddField(
            model_name='conteo',
            name='acta_img',
            field=models.ImageField(blank=True, null=True, upload_to='acta/%Y/%m/%d/%h', verbose_name='Imagen de Acta de Sugrafio'),
        ),
        migrations.AddField(
            model_name='conteo',
            name='hojatabajo_img',
            field=models.ImageField(blank=True, null=True, upload_to='hojatabajo/%Y/%m/%d/%h', verbose_name='Imagen de Hoja de Trabajo'),
        ),
        migrations.AlterField(
            model_name='conteo',
            name='papeletasobreante',
            field=models.IntegerField(default=0, verbose_name='Cantidad de Papeletas no Utilizadas'),
        ),
        migrations.AlterField(
            model_name='conteo',
            name='votocid',
            field=models.IntegerField(default=0, help_text='Comunidad de Integracion Democratica', verbose_name='Votos en C.I.D'),
        ),
        migrations.AlterField(
            model_name='conteo',
            name='votomts',
            field=models.IntegerField(default=0, help_text='Movimiento Tercer Sistema', verbose_name='Votos en M.T.S'),
        ),
        migrations.AlterField(
            model_name='conteo',
            name='votopst',
            field=models.IntegerField(default=0, help_text='Pando Somos Todos', verbose_name='Votos en P.S.T'),
        ),
    ]
