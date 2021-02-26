from django.db import models
from django.conf import settings
#from apps.usuarios.models import EstadoModel
from apps.geolocalizacion.models import Localidad,Ubicacion
import uuid
import time

class EstadoModel(models.Model):
    #id = models.UUIDField('id', default=uuid.uuid4, primary_key=True, unique=True, null=False, blank=False,editable=False)
    descripcion = models.TextField('descripcion', blank=True, null=True)
    direccion_ip = models.GenericIPAddressField(blank=True, null=True)
    creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modificacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    estado = models.BooleanField(default=True)
    #uc = models.CharField(max_length=100, blank=True,null=True)
    #uc = models.ForeignKey(Usuario,blank=True,null=True,on_delete=models.CASCADE)#usuario creo
    uc = models.IntegerField(blank=True, null=True)
    #um =models.ForeignKey(User,on_delete=models.CASCADE)#usuario modifico
    #um = models.CharField(max_length=100, blank=True,null=True)
    um = models.IntegerField(blank=True,null=True)

    class Meta:
        abstract = True

class Recinto(EstadoModel):
    localidad = models.ForeignKey(Localidad, null=True, blank=True, on_delete=models.CASCADE)
    nombrerecinto = models.CharField(max_length=100, blank=False, null=True,verbose_name='Nombre Recinto o Unidad Educativa',
                                     help_text='Ingrese Nombre del Recinto o Unidad Educativa')
    numerorecinto = models.CharField(max_length=100, blank=False, null=True, verbose_name='Sigla Recinto',
                                     help_text='Ingrese Sigla Recinto')
    recintomesa = models.IntegerField(default=0,verbose_name='Recinto en Mesa')
    recintohabilitado = models.IntegerField(default=0, verbose_name='Habilitado en Recinto')

    def __str__(self):
        return '%s %s' % (self.localidad.nombrelocalidad,self.nombrerecinto)

class Mesa(EstadoModel):
    recinto = models.ForeignKey(Recinto, null=True, blank=True, on_delete=models.CASCADE)
    codigomesa = models.CharField(max_length=100, blank=True, null=True, verbose_name='Codigo de Mesa',
                                  help_text='Ingrese Codigo de Mesa')
    numeromesa = models.CharField(max_length=100, blank=False, null=True,verbose_name='Numero de Mesa',
                                     help_text='Ingrese su Numero de Mesa')
    mesahabilitado = models.IntegerField(default=0, verbose_name='Habilitado en Mesa')
    def __str__(self):
        return "%s %s %s" % (self.recinto.localidad.nombrelocalidad,self.recinto.nombrerecinto,self.numeromesa)

class Sufragio(EstadoModel):
    tiposugrafio = models.CharField(max_length=100, blank=False, null=True,verbose_name='Nombre Tipo Recuento de Voto',
                                     help_text='Ingrese Tipo Recuento de Voto')
    def __str__(self):
        return "%s" % (self.tiposugrafio)

def img_acta(self, filename):
    hash_ = int(time.time())
    return "%s/%s/%s" % ("acta", hash_, filename)

def img_hojatrabajo(self, filename):
    hash_ = int(time.time())
    return "%s/%s/%s" % ("hojatrabajo", hash_, filename)

class Conteo(EstadoModel):
    delegadomesa = models.CharField(max_length=100, blank=True, null=True,verbose_name='Delegado de Mesa',help_text='Ingrese su Nombre o C.I')
    presidentemesa = models.CharField(max_length=100, blank=True, null=True,verbose_name='Presidente de Mesa',help_text='Ingrese su Nombre o C.I')

    sufragio = models.ForeignKey(Sufragio, null=True, blank=True, on_delete=models.CASCADE)
    codigo_conteo = models.UUIDField('codigo_conteo', default=uuid.uuid4, unique=True, null=False, blank=False, editable=False)
    mesa = models.ForeignKey(Mesa, null=True, blank=True, on_delete=models.CASCADE)
    #totalpapeletas = models.CharField(max_length=100, blank=False, null=True, verbose_name='Total de Papeletas',help_text='Ingrese Total de Papeletas')
    totalpapeletas = models.IntegerField(default=0,verbose_name='Papeletas o Habilitados')

    #votovida = models.IntegerField(default=0, verbose_name='Votos en VIDA',help_text='Vision Democratica Amazonica')
    votocid = models.IntegerField(default=0, verbose_name='Votos en C.I.D',help_text='Comunidad de Integracion Democratica')
    votomasipsp = models.IntegerField(default=0, verbose_name='Votos MAS IPSP',help_text='Movimiento Al Socialismo IPSP')
    votopanbol = models.IntegerField(default=0, verbose_name='Votos PAN-BOL',help_text='Partido de Accion Nacional Boliviano')
    votopst = models.IntegerField(default=0, verbose_name='Votos en P.S.T',help_text='Pando Somos Todos')
    votomts = models.IntegerField(default=0, verbose_name='Votos en M.T.S',help_text='Movimiento Tercer Sistema')
    votofpv = models.IntegerField(default=0, verbose_name='Votos en FPV', help_text='Frente Para la Victoria')
    votopaso = models.IntegerField(default=0, verbose_name='Votos en PASO', help_text='Poder Amazonico Social')
    votomda = models.IntegerField(default=0, verbose_name='Votos en MDA', help_text='Movimiento Democratica Autonomista')

    votovalidos = models.IntegerField(default=0, verbose_name='Votos Validos')
    votoblanco = models.IntegerField(default=0, verbose_name='Votos en Blancos')
    votonullo = models.IntegerField(default=0, verbose_name='Votos en Nulos')

    marcadopapeleta = models.IntegerField(default=0, verbose_name='Numero Papeleta Marcados')

    #2
    nropapeletasobrante = models.IntegerField(default=0, verbose_name='Numero Papeleta Sobrante')

    papeletasobreante = models.IntegerField(default=0, verbose_name='Cantidad de Papeletas no Utilizadas')
    carnetssobrantes = models.IntegerField(default=0, verbose_name='Carnet Sobrante')
    #1
    verificacioncipapeleta = models.BooleanField(default=0, verbose_name='C.I. y Papeletas')

    #3 editable=False,
    total = models.IntegerField(default=0,null=True,blank=True, verbose_name='Total de Votos Validos')
    #total = models.FloatField(default=0)

    cerrarpapeleta = models.IntegerField(default=0, verbose_name='Papeleta Mesa')

    acta_img = models.ImageField(verbose_name='Foto de Acta de Sugrafio', upload_to=img_acta, blank=True,
                                    null=True)

    hojatabajo_img = models.ImageField(verbose_name='Foto de Hoja de Trabajo', upload_to=img_hojatrabajo, blank=True,
                                    null=True)

    ubicacion = models.ForeignKey(Ubicacion, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        #3
        self.total = self.votopst + self.votopaso + self.votopanbol + self.votocid \
                     + self.votomda + self.votomts + self.votofpv + self.votomasipsp
        #1
        if(self.papeletasobreante != self.carnetssobrantes):
            self.verificacioncipapeleta = 0
        else:
            self.verificacioncipapeleta = 1
        #2
        self.marcadopapeleta = self.total + self.votonullo + self.votoblanco

        #self.nropapeletasobrante = self.total + self.votovalidos + self.votonullo + self.votoblanco - self.totalpapeletas
        self.nropapeletasobrante = self.totalpapeletas - self.marcadopapeleta
        #4
        self.cerrarpapeleta = self.marcadopapeleta + self.nropapeletasobrante
        super(Conteo,self).save()

    class Meta:
        ordering = ['-creacion']
        verbose_name_plural = "Papeletas"