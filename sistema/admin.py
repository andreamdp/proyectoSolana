# -*- encoding: utf-8 -*-
from django.contrib import admin
from sistema.models import *

from django.contrib.admin.widgets import ForeignKeyRawIdWidget
from django import forms


class RecursoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'name', 'descripcion')
    search_fields = ('name','tipo__name','descripcion',)
   # raw_id_fields = ('tipo',)
  
class TipoRecursoAdmin(admin.ModelAdmin):
    list_display = ('name', 'descripcion')
    search_fields = ('name','descripcion',)

class UnidadInline(admin.TabularInline):
    model = Unidad
    extra = 1

class UnidadAdmin(admin.ModelAdmin):
    list_display = ('name', 'abreviacion', 'descripcion')
    search_fields = ('name','descripcion',)
#    inlines = [UnidadInline]

class CobroAdmin(admin.ModelAdmin):
    search_fields = ('name','descripcion')

class ObraAdmin(admin.ModelAdmin):
    search_fields = ('name','descripcion')

class EstadoAdmin(admin.ModelAdmin):
    search_fields = ('name','descripcion')

class ChapaAdmin(admin.ModelAdmin):
    search_fields = ('name','descripcion')

class Estructura1Admin(admin.ModelAdmin):
    search_fields = ('name','descripcion')

class Estructura2Admin(admin.ModelAdmin):
    search_fields = ('name','descripcion')

class TelefonoAdmin(admin.ModelAdmin):
    search_fields = ('name','descripcion')


admin.site.register(Provincia)
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Titulo)
admin.site.register(Recurso,RecursoAdmin)
admin.site.register(TipoRecurso)
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(TipoCobro, CobroAdmin)
admin.site.register(TipoObra, ObraAdmin)
admin.site.register(TipoEstado, EstadoAdmin)
admin.site.register(TipoChapa, ChapaAdmin)
#admin.site.register(TipoEstructura1, Estructura1Admin)
#admin.site.register(TipoEstructura2, Estructura2Admin)
admin.site.register(TipoTelefono, TelefonoAdmin)
#admin.site.register(Banco)
