from django.db import models
#from apps.usuarios.models import EstadoModel
from django.utils.translation import ugettext_lazy as _
from django.forms import model_to_dict
"""
#Informacion
TimeStampModel()

Ubicacion()
Distrito()
Barrio(Distrito)
Direccion(Ubicacion,Barrio)

Departamentos()
Provincias(Departamentos)
Municipios(Provincias)
"""

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


class Ubicacion(EstadoModel):
    latitudubicacion = models.CharField(max_length=30, blank=False, null=False,
                                              verbose_name = 'Latitud')
    longitudubicacion = models.CharField(max_length=30, blank=False, null=False,
                                              verbose_name = 'Longitud')
    descripcionubicacion = models.CharField(max_length=150, blank=True, null=True,
                                              verbose_name = 'Descripcion de la Ubicacion')
    def __str__(self):
        return '%s %s' % (self.latitudubicacion,self.longitudubicacion)

    class Meta:
        verbose_name_plural = "Ubicaciones"




class Departamentos(EstadoModel):
    nombredepartamentos = models.CharField(max_length=50, blank=True, null=True,unique=True,
                                     verbose_name='Departamento',
                                     help_text='Ingrese su Nombre de Departamento')
    sigladepartamentos = models.CharField(max_length=15, blank=True, null=True,
                                     verbose_name='Sigla del Departamento',
                                     help_text='Ingrese la Sigla de Departamento')
    def __str__(self):
        return '%s %s' % (self.nombredepartamentos, self.sigladepartamentos)

    class Meta:
        verbose_name_plural = "Departamentos"

class Provincias(EstadoModel):
    departamentos = models.ForeignKey(Departamentos, null=True, blank=True, on_delete=models.CASCADE)
    nombreprovincias = models.CharField(max_length=50, blank=True, null=True,unique=True,
                                     verbose_name='Provincia',
                                     help_text='Ingrese su Nombre Provincia')
    siglaprovincias = models.CharField(max_length=15, blank=True, null=True,
                                     verbose_name='Sigla Provinvia',
                                     help_text='Ingrese la Sigla Provincia')
    def __str__(self):
        return '%s %s' % (self.departamentos.nombredepartamentos,self.nombreprovincias)

    class Meta:
        verbose_name_plural = "Provincias"

class Municipios(EstadoModel):
    provincias = models.ForeignKey(Provincias, null=True, blank=True, on_delete=models.CASCADE)
    nombremunicipios = models.CharField(max_length=50, blank=True, null=True,
                                     verbose_name='Municipio',
                                     help_text='Ingrese su Nombre Municipio')
    siglamunicipios  = models.CharField(max_length=15, blank=True, null=True,
                                     verbose_name='Sigla Municipio',
                                     help_text='Ingrese la Sigla Municipio')
    def __str__(self):
        return '%s %s' % (self.provincias, self.nombremunicipios)

    class Meta:
        verbose_name_plural = "Municipios"

class Localidad(EstadoModel):
    municipios = models.ForeignKey(Municipios, null=True, blank=True, on_delete=models.CASCADE)
    nombrelocalidad = models.CharField(max_length=50, blank=True, null=True,
                                     verbose_name='Ciudad Localidad',
                                     help_text='Ingrese el Nombre Ciudad Localidad')

    def __str__(self):
        return '%s %s' % (self.municipios, self.nombrelocalidad)

    class Meta:
        verbose_name_plural = "Localidades"
        ordering = ['-creacion']

class Distrito(EstadoModel):
    localidad = models.ForeignKey(Localidad, null=True, blank=True, on_delete=models.CASCADE)
    numerodistrito = models.IntegerField(blank=True, null=True,
                                              verbose_name = 'Numero del Distrito',
                                              help_text = 'Ingrese el Numero del Distrito')
    nombredistrito = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Nombre Distrito',
                                              help_text = 'Ingrese del Nombre Distrito')
    sigladistrito = models.CharField(max_length=10, blank=True, null=True,
                                              verbose_name = 'Sigla del Distrito',
                                              help_text = 'Ingrese la Sigla del Distrito')
    def __str__(self):
        return '%s %s' % (self.numerodistrito,self.nombredistrito)

    class Meta:
        verbose_name_plural = "Distritos"

class Barrio(EstadoModel):
    distrito = models.ForeignKey(Distrito,null=True,blank=True,on_delete=models.CASCADE)
    nombrebarrio = models.CharField(max_length=50, blank=True, null=True,unique=True,
                                              verbose_name = 'Nombre del Barrio',
                                              help_text = 'Ingrese Nombre del Barrio')
    siglabarrio = models.CharField(max_length=20, blank=True, null=True,
                                              verbose_name = 'Sigla del Barrio',
                                              help_text = 'Ingrese Sigla del Barrio')
    detallebarrio = models.CharField(max_length=255, blank=True, null=True,
                                              verbose_name = 'Detalle del Barrio',
                                              help_text = 'Ingrese Detalle del Barrio')

    def __str__(self):
        return '%s' % (self.nombrebarrio)
        #return '%s %s' % (self.distrito.numerodistrito, self.nombrebarrio)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = "Barrios"

class Direccion(EstadoModel):
    ubicacion = models.ForeignKey(Ubicacion,null=True,blank=True,on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio,null=False,blank=False,on_delete=models.CASCADE)

    zonadireccion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Zona',
                                              help_text = 'Ingrese Nombre de la Zona')
    referenciadireccion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Referencia',
                                              help_text = 'Ingrese Referencia')
    viadireccion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Nombre de la Via',
                                              help_text = 'Ingrese Nombre de la Via')
    calledireccion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Nombre de la Calle',
                                              help_text = 'Ingrese Nombre de la Calle')
    numerocasadireccion = models.CharField(max_length=20, blank=True, null=True,
                                              verbose_name = 'Numero de Casa',
                                              help_text = 'Ingrese Numero de Casa')
    avenidadireccion = models.CharField(max_length=50, blank=True, null=True,
                                              verbose_name = 'Nombre de la Avenida',
                                              help_text = 'Ingrese Nombre de la Avenida')

    def __str__(self):
        return '%s %s %s' % (self.barrio,self.avenidadireccion,self.numerocasadireccion)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = "Direccion"

"""
    direccion = models.CharField(_("Direccion"), max_length=255, blank=True, null=True)
    calle = models.CharField(_("Calle"), max_length=55, blank=True, null=True)
    codigo_postal = models.CharField(_("Codigo Postal/Postal"), max_length=64, blank=True, null=True)
"""
