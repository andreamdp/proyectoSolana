# -*- encoding: utf-8 -*-
from django.db import models
from sistema.models import *
from clientes.models import *
from smart_selects.db_fields import ChainedForeignKey
from thumbs import ImageWithThumbsField
from pruebas.models import *
from django.db.models.fields import CharField
from django.contrib.localflavor.us.us_states import STATE_CHOICES

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
       # ('Estructura Hormigon', 'Estructura Hormigón'),
       # ('Estructura Metalica', 'Estructura Metálica'),
       # ('Cerramientos', 'Cerramientos'),
#	('Cubierta Metalica', 'Cubierta Metálica'),
#	('Entrepiso', 'Entrepiso'),
#	('Instalaciones', 'Instalaciones'),
#	('Varios', 'Varios'),
#	('Subtotales', 'Subtotales'),
        ('EH', 'Estructura Hormigón'),
        ('EM', 'Estructura Metálica'),
        ('C', 'Cerramientos'),
	('CM', 'Cubierta Metálica'),#
	('E', 'Entrepiso'),
	('I', 'Instalaciones'),
	('V', 'Varios'),
	('S', 'Subtotales'),
    )

 categoria = models.CharField(max_length=2, choices=choice) 
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
       #categoria = models.CharField(max_length=2, choices=CategoriaChoice)       
       nombre = models.CharField(max_length=25)
       categoria = models.ForeignKey(Categoria, related_name='+')
      
       class Meta:
		verbose_name = 'SubCategoria'        
		verbose_name_plural = "Administrar SubCategorias"
       def __unicode__(self):
	        return u'%s' % (self.nombre)




class Presupuesto(models.Model):       
	cliente = models.ForeignKey(Cliente)
	obra = ChainedForeignKey(
		ConjuntoObra, 
		chained_field="cliente",
		chained_model_field="cliente", 
		show_all=False, 
		auto_choose=True
    	)
        total = models.IntegerField( null=True, blank=True)



        #detalle1 = models.ForeignKey('Detalle', related_name='+')
       # tareas = models.DecimalField('Tareas preliminares',default = 0.0,max_digits = 7, decimal_places = 2)
	#precio = models.FloatField('Precio', null=True, blank=True, default = 0.0)
        #choice = (
        # ('EH', 'Estructura Hormigón'),
        # ('EM', 'Estructura Metálica'),
        # ('C', 'Cerramientos'),
	# ('CM', 'Cubierta Metálica'),
	# ('E', 'Entrepiso'),
	# ('I', 'Instalaciones'),
	# ('V', 'Varios'),
	# ('S', 'Subtotales'),
        #)
        #categoria = models.CharField(max_length=2, choices=choice)   
     	#concepto =  ChainedForeignKey(
        #  SubCategoria, 
        #  chained_field="categoria",
        #  chained_model_field="categoria", 
        #  show_all=False, 
        #  auto_choose=True
        #)
      #  presupuesto = models.ForeignKey('Presupuesto', related_name='+' )
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
       
        
       # categoria = models.CharField(max_length=2, choices=CategoriaChoice)   
        categoria = models.ForeignKey(Categoria, related_name='+')
	
	concepto =  ChainedForeignKey(
          SubCategoria, 
          chained_field="categoria",
          chained_model_field="categoria", 
          show_all=False, 
          auto_choose= True
        )
        presupuesto = models.ForeignKey(Presupuesto)
	#categoria = models.ForeignKey(Categoria, related_name='+')
	@property
        def total(self):
          return self.precio + 100

        def __unicode__(self):
	   return '%s' % (self.precio+20)

	def __unicode__(self):
	        return u'%s' % (self.categoria)






