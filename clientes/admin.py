# -*- encoding: utf-8 -*-
from django.contrib import admin
from auth import models
from sistema.models import *
from clientes.models import *
from django.forms import TextInput, Textarea
#from pruebas.models import *
#from pruebas.admin import *

class TelefonoInline(admin.TabularInline):
    model = Telefono
    extra = 1

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1

class ClienteOptions(admin.ModelAdmin):
#	list_display = ('nombre','cliente','ciudad','estado')
    list_display = ('__unicode__', 'razon_social', 'ciudad')
    list_filter = ('ciudad',)
    list_display_links = ('__unicode__', 'razon_social',)
    search_fields = ('nombre', 'apellido', 'cliente_nro','cuit')
    fieldsets = (
		('Información General',
		       {'fields':(('titulo', 'nombre','apellido'),('razon_social', 'cuit','cliente_nro')    )}),
#		('Datos de Contacto',
#		       {'fields':(('telefono_fijo', 'telefono_celular'), 'email')}),
		('Ubicación', { 
			'classes': ['collapse', 'wide', 'extrapretty'],
		       'fields':(('direccion','altura'),('pais','provincia', 'ciudad'))
			}),
            	)

    inlines = [TelefonoInline,EmailInline]
from django import forms
from django.forms import ModelChoiceField
from smart_selects.db_fields import ChainedForeignKey

class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        # Return a string of the format: "firstname lastname (username)"
        return "%s"%(obj.id)

class CostoAdminForm(forms.ModelForm):
  
    class Meta:
        model = Costo
        
   
    #        self.fields['recurso'].queryset =  Recurso.objects.all()
           
   #         if self.instance:
   #           valor_propiedad = self.instance.tipo
   #   '''      #  self.fields['recurso'].queryset = Recurso.objects.filter(tipo = valor_propiedad)
        
      #  if inst:if db_field.name == 'director_obra':
         #   kwargs['queryset'] = User.objects.filter(groups__name='director de Obra')
        #self.fields['recurso'].queryset = Recurso.objects.filter(tipo=2 )
            #self.fields['unit'].queryset = project_unit.objects.filter(project=inst.project)
    '''class Meta:
        model = Costo
    def __init__(self, *arg, **kwargs):
        super(CostoAdminForm, self).__init__(*arg, **kwargs)
        #self.recurso = [(csc.id,csc.name) for csc in Recurso.objects.all()]
'''
class CostoInline(admin.TabularInline):
    form = CostoAdminForm
    model = Costo
    
#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#if db_field.name == 'temporada':
#kwargs["queryset"] =
#models.Temporada.objects.filter(serie=request.user)
#return super(capitulo_inline, self).formfield_for_foreignkey(db_field,
#request, **kwargs)
    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #    if db_field.name == 'recurso':
    #        kwargs['queryset'] = Recurso.objects.filter(self.fields['tipo'] = 2 )
    #        return super(CostoInline, self).formfield_for_foreignkey(db_field,request, **kwargs)
    formfield_overrides = {
	models.TextField: {'widget': Textarea(attrs={'rows':2, 'cols':50})},
        models.DecimalField: {'widget': TextInput(attrs={'size':'8'})},
    }
    fieldsets = (							#aca se podria definir el orden de las columnas
		(None, {
			'fields':('tipo', 'recurso','cantidad','unidad','valor_unitario','total','observaciones',)
			}),
	        )
    extra = 1

   # raw_id_fields = ('tipo',)
    #
    

class ConjuntoCostoOptions(admin.ModelAdmin):
    #list_display = ('obra','cliente', 'ciudad')
    #list_filter = ('cliente__ciudad','obra__estado')
    #list_display_links = ('cliente','obra',)
    #search_fields = ('cliente__nombre','cliente__razon_social','costo__observaciones')
    #fieldsets = (
#		(('Datos de la Obra'),
#               		{'fields':(('cliente', 'obra'),)}),
		#	{'description': ('hola'),}),
#	        )
   
    inlines = [CostoInline]
   
    
    def ciudad(self, obj):
        return obj.obra.getCiudad()
    ciudad.short_description = 'Ciudad de la Obra'

    def upper_case_cliente(self, obj):
      return ("%s" % (obj.cliente)).upper()

class ObraInline(admin.StackedInline):
     model = Obra 
     extra = 1 
     classes = ('collapse closed',)
     #list_display = ('obra')
     fieldsets = (
	('Dimensiones',
		       {'fields':(('largo', 'ancho', 'superficie' ),)}),	
	('Estructura', 
		       {#'classes': ['collapse', 'wide', 'extrapretty'],
		        'fields':(('cubierta','hierro', 'canaletas'),)
			}),
	('Cerramiento', 
		       {#'classes': ['collapse', 'wide', 'extrapretty'],
		        'fields':(('chapa','perimetroChapa','altoChapa','superficieChapa'),
				  ('bloque','perimetroBloque','altoBloque','superficieBloque'))
			}),		
	('Cubierta', 
               {'fields':(('tipoChapa','anchoCubierta','largoCubierta','superficieCubierta'),) }),
        ('Varios', 
		       {'classes': ['collapse', 'wide', 'extrapretty'],
		       'fields':(('porton','fieltro','tipo_obra'),('observacion' ))}),	
        )

#     formfield_overrides = {
#         models.TextField: {'widget': RichTextEditorWidget},
#     }


class CobroInline(admin.TabularInline):
    model = Cobro
    classes = ('collapse closed',)
    formfield_overrides = {
	models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':80})},
    }

class ConjuntoObraOptions(admin.ModelAdmin):

	list_display = ('nombre','cliente','ciudad','estado','getDirectorObra')
        list_filter = ('ciudad','estado',)
        list_display_links = list_display
#        list_editable = ('estado',)
#        raw_id_fields = ('cliente',)
	fieldsets = (
	       ('Datos de la Obra',
			       {'fields':(('cliente', 'nombre'),('ciudad','estado','director_obra' ),)}),		
	)
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
            if db_field.name == 'director_obra':
        	kwargs['queryset'] = User.objects.all()#filter(groups__name='director de Obra')
            return super(ConjuntoObraOptions, self).formfield_for_foreignkey(db_field, request, **kwargs)       	

	inlines = [ObraInline,CobroInline]

class DetalleInline(admin.TabularInline):
    model = Detalle
    fieldsets = (							#aca se podria definir el orden de las columnas
		(None, {
			'fields':('categoria','concepto','precio')
			}),
	        )

    extra = 1  



class DetalleAdmin(admin.ModelAdmin):
 class Meta:
        model = Detalle
 list_display = ('precio','total')
 
 def get_changelist(self, request):
        return MyChangeList

class PresupuestoOptions(admin.ModelAdmin):
    class Meta:
        model = Presupuesto
   # search_fields = ['cliente']
   # search_fields_verbose = ['cliente']
    list_display = ('obra','cliente','totalPresupuesto')
    list_filter = ('cliente__ciudad',)
    list_display_links = list_display
    search_fields = ('nombre', 'apellido', 'cliente_nro','cuit')
    template = 'pruebas/tabular.html'
#    readonly_fields = ('monto_obra',)
   # formfield_overrides = {
   #     models.TextField: {'widget': MarkItUpWidget},
   # }
    #readonly_fields = ('totalHormigonReal','totalMetalicaReal','totalCerramientoReal', 'totalCubiertaMetalicaReal','totalEntrepisoReal','totalInstalacionesReal', 'totalVariosReal',  )
    fieldsets = (							#aca se podria definir el orden de las columnas
		 (None, {
			'fields':(('cliente','obra'),),#, 'total'
			}),
	         
                 #(None, {
	#		'fields':('categoria','concepto')
	#		}),
	         )
        
   
    extra = 1  
  #  form = PresupuestoForm
    class Media:
        css = {
            'all': ("estilo.css",)
     }
   
    #inlines = [CostoInline]
    inlines = [DetalleInline]
    

class PresuInline(admin.TabularInline):
    model = PresupuestoOptions
    classes = ('collapse closed',)
    

    
class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre')

admin.site.register(Cliente,ClienteOptions)
admin.site.register(ConjuntoObra,ConjuntoObraOptions)
admin.site.register(Cobro)
admin.site.register(ConjuntoCosto,ConjuntoCostoOptions)
admin.site.register(Presupuesto,PresupuestoOptions)
admin.site.register(SubCategoria, SubCategoriaAdmin)
#admin.site.register(Categoria)

