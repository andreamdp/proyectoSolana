# -*- encoding: utf-8 -*-
from django.db import models
#from smart_selects.db_fields import ChainedForeignKey

class Pais(models.Model):
    name = models.CharField('Nombre', max_length = 50)

    class Meta:
	verbose_name = "País"        
	verbose_name_plural = "Paises"

    def __unicode__(self):
        return self.name

class Provincia(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    pais = models.ForeignKey(Pais)

    class Meta:
        verbose_name = "Provincia"
	verbose_name_plural = "Provincias"

    def __unicode__(self):
        return self.name

class Ciudad(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    provincia = models.ForeignKey(Provincia)

    class Meta:
	verbose_name = "Ciudad"        
	verbose_name_plural = "Ciudades"

    def __unicode__(self):
        return self.name

class Titulo(models.Model):       
    name = models.CharField('Nombre', max_length=15)

    class Meta:
	verbose_name = 'Título'     
	verbose_name_plural = 'Títulos'

    def __unicode__(self):
        return self.name


class TipoRecurso(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
    
    class Meta:
        verbose_name = "Tipo de Recurso"
	verbose_name_plural = "Tipos de Recursos"

    def __unicode__(self):
        return self.name

class Unidad(models.Model):       
    name = models.CharField('Nombre', max_length=20)
    abreviacion = models.CharField(max_length=10)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
   

    class Meta:
	verbose_name = 'Unidad'     
	verbose_name_plural = 'Unidades'

    def __unicode__(self):
        return self.abreviacion






class Recurso(models.Model):
    tipo = models.ForeignKey(TipoRecurso, related_name='recurso_tipo')
    #country = models.ForeignKey(Country, related_name='recurso_tipo')
    unidad = models.ForeignKey(Unidad) #esto es de prueba
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
    
    class Meta:
        verbose_name = "Nombre de Recurso"
	verbose_name_plural = "Nombre de Recursos"

    def __unicode__(self):
	return u'%s' % (self.name)



class TipoCobro(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
    
    class Meta:
        verbose_name = "Tipo de Cobro"
	verbose_name_plural = "Tipos de Cobros"

    def __unicode__(self):
        return self.name

class TipoObra(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
    
    class Meta:
        verbose_name = "Tipo de Obra"
	verbose_name_plural = "Tipos de Obra"

    def __unicode__(self):
        return self.name

class TipoEstado(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
    
    class Meta:
        verbose_name = "Tipo de Estado"
	verbose_name_plural = "Tipos de Estados"

    def __unicode__(self):
        return self.name

class TipoChapa(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
    
    class Meta:
        verbose_name = "Tipo de Chapa"
	verbose_name_plural = "Tipos de Chapas"

    def __unicode__(self):
        return self.name

class TipoEstructura1(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
    
    class Meta:
        verbose_name = "Tipo de Estructura Cubierta"
	verbose_name_plural = "Tipos de Estructuras Cubiertas"

    def __unicode__(self):
        return self.name

class TipoEstructura2(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
    
    class Meta:
        verbose_name = "Tipo de Estructura Hierro"
	verbose_name_plural = "Tipos de Estructuras Hierros"

    def __unicode__(self):
        return self.name

class TipoTelefono(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
    
    class Meta:
        verbose_name = "Tipo de Teléfono"
	verbose_name_plural = "Tipos de Teléfonos"

    def __unicode__(self):
        return self.name

class Banco(models.Model):
    name = models.CharField('Nombre', max_length = 50)
    descripcion = models.TextField('Descripción', max_length = 100, null = True, blank = True)
    
    class Meta:
        verbose_name = "Banco"
	verbose_name_plural = "Bancos"

    def __unicode__(self):
        return self.name
