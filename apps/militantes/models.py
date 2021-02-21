from django.db import models
from apps.usuarios.templatetags.utils import SEXOS,TIPO_SOCIO,VOTAR
import uuid
from apps.usuarios.models import Usuario,EstadoModel

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Persona(EstadoModel):
    nombrepersona = models.CharField(max_length=100, blank=False, null=True,verbose_name='Nombre',
                                     help_text='Ingrese su Nombre')
    paternopersona = models.CharField(max_length=100, blank=True, null=True,verbose_name='Apellido Paterno',
                                      help_text = 'Ingrese su Apellido Paterno')
    maternopersona = models.CharField(max_length=100, blank=True, null=True,
                                      verbose_name='Apellido Materno',
                                      help_text='Ingrese su Apellido Materno')
    cipersona = models.CharField(max_length=20, blank=False, null=True,unique=True,#cambiar esta obligatorio numero carnet cliente
                                 verbose_name='Cedula de Identidad',
                                 help_text = 'Ingrese su Numero de Cedula de Identidad')
    generopersona = models.BooleanField(default=1,choices=SEXOS,
                                        verbose_name='Genero',
                                        help_text = 'Ingrese Genero')
    nacimientopersona = models.DateField(blank=True,null=True,
                                         verbose_name = 'Fecha de nacimiento',
                                         help_text = 'Seleccione su fecha de nacimiento')

    def __str__(self):
        return '%s %s %s %s' % (self.cipersona,self.nombrepersona,self.paternopersona,self.maternopersona)

    def save(self):
        self.nombrepersona = self.nombrepersona.title()
        #self.paternopersona =self.paternopersona.title()
        #self.maternopersona = self.maternopersona.title()
        super(Persona, self).save()

    class Meta:
        verbose_name_plural = "Personas"
        ordering = ['-creacion']

class Institucion(EstadoModel):
    nombreinstitucion = models.CharField(max_length=250, blank=False, null=True,
                                     verbose_name='Nombre Institucion',
                                     help_text='Ingrese su Nombre Institucion')
    siglainstitucion = models.CharField(max_length=15, blank=True, null=True,
                                     verbose_name='Sigla Institucion',
                                     help_text='Ingrese la Sigla Institucion')
    nitinstitucion = models.CharField(max_length=25, blank=True, null=True,verbose_name='Nit de Empresa',help_text='Ingrese el Nit o Número de Identifican Tributaria')
    #nitinstitucion = models.CharField(max_length=25, blank=True, null=True, unique=True,verbose_name='Nit de Empresa',help_text='Ingrese el Nit o Número de Identifican Tributaria')

    def __str__(self):
        return '%s %s' % (self.nombreinstitucion,self.nitinstitucion)

#self.nombreinstitucion = self.nombreinstitucion.upper()
#self.nombreinstitucion = self.nombreinstitucion.lower().capitalize()
    def save(self):
        self.nombreinstitucion = self.nombreinstitucion.upper()
        #self.nombreinstitucion = self.nombreinstitucion.title()
        #self.siglainstitucion =self.siglainstitucion.upper()
        super(Institucion, self).save()

    class Meta:
        verbose_name_plural = "Instituciones"
        ordering = ['-creacion']

"""
def socio_numero():
    j = "JUNTOS-"
    e = "-"
    try:
        inv = Socio.objects.all().order_by('-creacion')[0].codigosocio
        #print(inv)
        #return int(inv) + 1
        return j+str(int(inv) + 1)+e
    except:
        return j+str(2020)+e
"""

class Socio(EstadoModel):
    codigosocio = models.TextField(blank=True, null=True, editable=False)
    codigo_qr = models.UUIDField('codigo_qr', default=uuid.uuid4, unique=True, null=False, blank=False,editable=False)
    persona = models.OneToOneField(Persona, null=True, blank=True, on_delete=models.CASCADE)
    #persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    tiposocio = models.BooleanField(default=1,choices=TIPO_SOCIO,verbose_name='Tipo de Socio',help_text = 'Ingrese Tipo de Socio')

    usuario = models.OneToOneField(Usuario, null=True, blank=True,on_delete=models.CASCADE)

    impresion = models.IntegerField(blank=True, null=True)
    informacion = models.CharField(max_length=60, blank=True, null=True,verbose_name='Informacion',help_text='Ingrese Informacion')

    def __str__(self):
        return "%s" % (self.codigo_qr)

    #def save(self):
    #    self.codigo_qr = "JunstosPando-"+str(self.codigo_qr)
    #    super(Socio, self).save()

    class Meta:
        verbose_name_plural = "Socios"
        ordering = ['-creacion']

@receiver(post_save, sender=Usuario)
def create_usuario_socio(sender, instance=None, created=False, **kwargs):
    if created:
        Socio.objects.create(usuario=instance)

def ultimo_numero():
    try:
        inv = Votar.objects.all().order_by('-creacion')[0].codigovotar
        #print(inv)
        return int(inv) + 1
    except:
        return 1

class Votar(EstadoModel):
    codigovotar = models.CharField(max_length=80, default=ultimo_numero)
    socio = models.OneToOneField(Socio, null=False, blank=False,unique=True, on_delete=models.CASCADE)
    tiposocio = models.BooleanField(default=1, choices=TIPO_SOCIO)

    def __str__(self):
        return "%s" % (self.socio)

    class Meta:
        verbose_name_plural = "Votantes"
        ordering = ['-creacion']

