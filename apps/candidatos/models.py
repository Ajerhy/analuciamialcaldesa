from django.db import models
from apps.militantes.models import Persona
from apps.usuarios.models import EstadoModel
import time

class Cargo(EstadoModel):
    titulo = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-creacion']
        verbose_name_plural = "Cargos"

def img_url(self, filename):
    hash_ = int(time.time())
    return "%s/%s/%s" % ("media", hash_, filename)

class Candidato(EstadoModel):
    titulo = models.CharField(max_length=250, blank=True, null=True)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, null=True, blank=True, on_delete=models.CASCADE)
    frase = models.CharField(max_length=250, blank=True, null=True)
    imagen = models.ImageField(verbose_name='Imagen de Candidato', upload_to=img_url, blank=True, null=True)

    link_facebook=models.CharField(verbose_name='facebook',max_length=100, blank=True, null=True)
    link_instagram=models.CharField(verbose_name='instagram',max_length=100, blank=True, null=True)
    link_youtube=models.CharField(verbose_name='youtube',max_length=100, blank=True, null=True)


    #def __str__(self):
    #    return '%s' % (self.cargo)

    def __str__(self):
        return '{} {}'.format(self.persona.nombrepersona,self.cargo)

    class Meta:
        ordering = ['-creacion']
        verbose_name_plural = "Candidatos"