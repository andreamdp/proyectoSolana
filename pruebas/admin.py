# -*- encoding: utf-8 -*-
#from django.forms.models import fields_for_model
from django.contrib import admin
from pruebas.models import *
from django.forms import TextInput, Textarea
from pruebas.forms import DetalleForm, PresupuestoForm
#from grappelli.actions import csv_export_selected
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.admin.views.main import ChangeList
from django.db.models import Count, Sum

class MyChangeList(ChangeList):

    def get_results(self, *args, **kwargs):
        super(MyChangeList, self).get_results(*args, **kwargs)
        q = self.result_list.aggregate(precio_sum=Sum('precio'))
        self.precio_count = q['precio_sum']

#class ConjuntoPresupuestoOptions(admin.ModelAdmin):
 #   inlines = [ObraInline,CobroInline]
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
			'fields':(('cliente','obra', 'total'),),
			}),
	         
                 #(None, {
	#		'fields':('categoria','concepto')
	#		}),
	         )
        
   
    extra = 1  
    form = PresupuestoForm
    class Media:
        css = {
            'all': ("estilo.css",)
     }
   
    #inlines = [CostoInline]
    inlines = [DetalleInline]
    

class PresuInline(admin.TabularInline):
    model = PresupuestoOptions
    classes = ('collapse closed',)
    
#class B_Admin(PresupuestoOptions):
    #fieldsets = [
    #         ('Specific to B', {'fields': ['total']}),
    #]
    #fieldsets.insert(0, PresupuestoOptions.fieldsets[0])
    #fieldsets.insert(5, PresupuestoOptions.fieldsets[5])
    
class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria','nombre')
from django.forms import ModelForm
from django.contrib.auth.models import User



#admin.site.register(Presupuesto,PresupuestoOptions)
admin.site.register(Categoria)
admin.site.register(SubCategoria, SubCategoriaAdmin)
##admin.site.register(B,B_Admin)
#admin.site.register(Detalle, DetalleAdmin)
