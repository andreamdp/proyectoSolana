# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Group, User
from sistema.models import *
from smart_selects.db_fields import ChainedForeignKey
from presupuesto import *
# Create your models here.

class Cliente(models.Model):       
    titulo = models.ForeignKey(Titulo, null = True, blank = True)
    nombre = models.CharField(max_length = 50, null = True, blank = True)
    apellido = models.CharField(max_length = 50 , null = True, blank = True)
    razon_social = models.CharField('Razón Social',max_length = 50, null = True, blank = True)
    cuit = models.PositiveIntegerField('Cuit/Cuil/DNI', max_length = 50, null = True, blank = True) 
    cliente_nro = models.PositiveIntegerField('Centro de Costo', null = True, blank = True)
    direccion = models.CharField(max_length = 200, null = True, blank = True)
    altura = models.PositiveIntegerField('Altura', null = True, blank = True) 
    ciudad = models.ForeignKey(Ciudad, null = True, blank = True)
    provincia = models.ForeignKey(Provincia, null = True, blank = True)
    pais = models.ForeignKey(Pais, null = True, blank = True)
    
    class Meta:
	verbose_name = 'Cliente'        
	verbose_name_plural = "Administrar Clientes"

    def __unicode__(self):
        return u'%s %s' % (self.nombre, self.apellido)

class Telefono(models.Model):
    tipo = models.ForeignKey(TipoTelefono)
    numero = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=80, null = True, blank = True)
    cliente = models.ForeignKey(Cliente)

    def __unicode__(self):
        return u'%s (%s)' % (self.numero, self.tipo)

class Email(models.Model):
    email = models.CharField(max_length = 50, default = '@', null = True, blank = True)
    cliente = models.ForeignKey(Cliente)

    def __unicode__(self):
        return self.email

class ConjuntoObra(models.Model): 
    nombre = models.CharField('Nombre de la Obra', max_length=50)
    cliente = models.ForeignKey(Cliente)
    ciudad = models.ForeignKey(Ciudad)
    estado = models.ForeignKey(TipoEstado, null=True, blank=True)
    director_obra = models.ForeignKey(User, null=True, blank=True)
 
    def __unicode__(self):
        return self.nombre

    def getCiudad(self):
        return self.ciudad
    getCiudad.short_description = 'Ciudad de la Obra'

    def getDirectorObra(self):
       	return self.director_obra.get_full_name()
    getDirectorObra.short_description = 'Director de Obra'

    class Meta:
	verbose_name_plural = "Administrar Obras"
        verbose_name = "Obra"

class Obra(models.Model):   
    conjunto_obra=models.ForeignKey(ConjuntoObra)
    #Dimensiones
    ancho = models.FloatField('Ancho', null=True, blank=True, default = 0.0)
    largo= models.FloatField('Largo', null=False, blank=True, default = 0.0)
    superficie= models.FloatField('Sup 2', null=False, blank=True, default = 0.0)
    #Estructura
    cubierta = models.ForeignKey(TipoEstructura1, null=True, blank = True)
    hierro = models.ForeignKey(TipoEstructura2, null=True, blank = True)
    #Cerramiento
    chapa = models.BooleanField(default=False)
    perimetroChapa = models.FloatField('Perim.', null=True, blank=True, default = 0.0)
    altoChapa = models.FloatField('Alto', null=True, blank=True, default = 0.0)
    superficieChapa = models.FloatField('Superficie',null=True, blank=True, default = 0.0)
    bloque = models.BooleanField(default=False)
    perimetroBloque = models.FloatField('Perim.', null=True, blank=True, default = 0.0)
    altoBloque = models.FloatField('Alto', null=True, blank=True, default = 0.0)
    superficieBloque = models.FloatField('Superficie',null=True, blank=True, default = 0.0)
    #cubierta
    tipoChapa=models.ForeignKey(TipoChapa, null=True, blank = True)
    anchoCubierta= models.FloatField('Ancho', null=True, blank=True, default = 0.0)
    largoCubierta=models.FloatField('Largo', null=True, blank=True, default = 0.0)
    superficieCubierta=models.FloatField('Superficie',null=True, blank=True, default = 0.0)
    fieltro= models.BooleanField(null=False, blank=True, default=False)
    #Varios
    porton= models.BooleanField('Portón', null=False, blank=True, default=False)
    canaletas= models.BooleanField('Canaletas', null=False, blank=True, default=False)
    observacion=models.TextField('Observaciones', null=False, blank=True)
    tipo_obra = models.ForeignKey(TipoObra)
#    presupuesto = models.ForeignKey(Presupuesto)

    class Meta:
        verbose_name = "Sub Obra"
        verbose_name_plural = "Obras"

 #   def __unicode__(self):
 #       return self.nombre

class ConjuntoCosto(models.Model):
    cliente = models.ForeignKey(Cliente)
    #cliente = models.OneToOneField(Cliente, primary_key=True)
    obra = ChainedForeignKey(
        ConjuntoObra, 
        chained_field="cliente",
        chained_model_field="cliente", 
        show_all=False, 
        auto_choose=True
    )

    def __unicode__(self):
        return str(self.obra)

    class Meta:
        verbose_name = "Costo de Obra"
        verbose_name_plural = "Administrar Costos de Obras"


class Costo(models.Model):
    conjunto_costo = models.ForeignKey(ConjuntoCosto)
#    tipo = ChainedForeignKey(
#        TipoRecurso, 
#        chained_field="tipo",
#        chained_model_field="tipo", 
#        show_all=False, 
#        auto_choose=True
#    )
    tipo = models.ForeignKey(TipoRecurso)
    recurso = ChainedForeignKey(
        Recurso, 
        chained_field="tipo",
        chained_model_field="tipo", 
        show_all=False, 
        auto_choose=True
    )
   #recurso = models.ForeignKey(Recurso)
    cantidad = models.DecimalField(null = True, blank = True, default = 0.0, max_digits = 5, decimal_places = 2)
    #unidad = models.ForeignKey(Unidad, null = True, blank = True)
    unidad  = ChainedForeignKey(
        Unidad, 
        chained_field="recurso",
        chained_model_field="recurso", 
        show_all=False, 
        auto_choose=True
    )
    valor_unitario = models.DecimalField(default = 0.0, max_digits = 5, decimal_places = 2)  
    total = models.DecimalField(default = 0.0, max_digits = 10, decimal_places = 2)  
    observaciones = models.TextField(max_length=50 , null = True, blank = True)

    def __unicode__(self):
        return "	"

'''
class ConjuntoCobro(models.Model):
    obra = models.ForeignKey(ConjuntoObra)

    def __unicode__(self):
        return str(self.obra)

    class Meta:
        verbose_name = "Cobro de Obra"
        verbose_name_plural = "Administrar Cobros de Obras"
'''

class Cobro(models.Model):
    conjunto_obra = models.ForeignKey(ConjuntoObra)
    tipo_cobro = models.ForeignKey(TipoCobro)
#    numero = models.PositiveIntegerField('Numero', null = True, blank = True)
#    banco = models.ForeignKey(Banco, null = True, blank = True)
    fecha = models.DateField()
    importe = models.DecimalField(default = 0.0, max_digits = 7, decimal_places = 2)  
    observaciones = models.TextField(max_length=50 , null = True, blank = True)

    def __unicode__(self):
	return u'%s (%s): %s' % (self.importe, self.fecha, self.observaciones)
#		u'%s (%s)' % (self.numero, self.tipo)

    class Meta:
        verbose_name = "Cobro"
        verbose_name_plural = "Administrar Cobros"

CategoriaChoice = (
         ('EH', 'Estructura Hormigón'),
         ('EM', 'Estructura Metálica'),
         ('C', 'Cerramientos'),
	 ('CM', 'Cubierta Metálica'),
	 ('E', 'Entrepiso'),
	 ('I', 'Instalaciones'),
	 ('V', 'Varios'),
	 ('S', 'Subtotales'),
)

class Categoria(models.Model):
 choice = (
        ('Estructura Hormigon', 'Estructura Hormigón'),
        ('Estructura Metalica', 'Estructura Metálica'),
        ('Cerramientos', 'Cerramientos'),
	('Cubierta Metalica', 'Cubierta Metálica'),
	('Entrepiso', 'Entrepiso'),
	('Instalaciones', 'Instalaciones'),
	('Varios', 'Varios'),
	('Subtotales', 'Subtotales'),

    )

 categoria = models.CharField(max_length=32, choices=choice) 
 class Meta:
		verbose_name = 'Categoria'        
		verbose_name_plural = "Administrar Categorias"     

 def __unicode__(self):
	        return u'%s' % (self.categoria)
class SubCategoria(models.Model):
       choice = (
         ('EH', 'Estructura Hormigón'),
         ('EM', 'Estructura Metálica'),
         ('C', 'Cerramientos'),
	 ('CM', 'Cubierta Metálica'),
	 ('E', 'Entrepiso'),
	 ('I', 'Instalaciones'),
	 ('V', 'Varios'),
	 ('S', 'Subtotales'),
	)
      
       nombre = models.CharField(max_length=25)
       categoria = models.ForeignKey(Categoria, related_name='+')
      
       class Meta:
		verbose_name = 'SubCategoria'        
		verbose_name_plural = "Administrar SubCategorias"
       def __unicode__(self):
	        return u'%s' % (self.nombre)




class Presupuesto(models.Model):       
	cliente = models.ForeignKey(Cliente, related_name='+')
	obra = ChainedForeignKey(
		ConjuntoObra, 
		chained_field="cliente",
		chained_model_field="cliente", 
		show_all=False, 
		auto_choose=True,
		related_name ="+",
    	)
        total = models.IntegerField( null=True, blank=True)

	class Meta:
		verbose_name = 'Presupuesto'        
		verbose_name_plural = "Administrar Presupuestos"



        def totalPresupuesto(self):
          c = Detalle.objects.filter(presupuesto=self.id)
          return sum([detalle.precio for detalle in c ])
	def __unicode__(self):
	        return u'%s (%s)' % (self.cliente, self.obra)

class Detalle(models.Model):
        precio = models.FloatField('Precio', null=True, blank=True, default = 0.0)
        categoria = models.ForeignKey(Categoria, related_name='+')
	
	concepto =  ChainedForeignKey(
          SubCategoria, 
          chained_field="categoria",
          chained_model_field="categoria", 
          show_all=False, 
          auto_choose= True
        )
        presupuesto = models.ForeignKey(Presupuesto, related_name='+')
	@property
        def total(self):
          return self.precio + 100

        def __unicode__(self):
	   return '%s' % (self.precio+20)

	def __unicode__(self):
	        return u'%s' % (self.categoria)
