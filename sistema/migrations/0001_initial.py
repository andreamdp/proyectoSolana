# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Pais'
        db.create_table('sistema_pais', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['Pais'])

        # Adding model 'Provincia'
        db.create_table('sistema_provincia', (
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Pais'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['Provincia'])

        # Adding model 'Ciudad'
        db.create_table('sistema_ciudad', (
            ('provincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Provincia'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['Ciudad'])

        # Adding model 'Titulo'
        db.create_table('sistema_titulo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('sistema', ['Titulo'])

        # Adding model 'TipoRecurso'
        db.create_table('sistema_tiporecurso', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['TipoRecurso'])

        # Adding model 'Unidad'
        db.create_table('sistema_unidad', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abreviacion', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('sistema', ['Unidad'])

        # Adding model 'Recurso'
        db.create_table('sistema_recurso', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recurso_tipo', to=orm['sistema.TipoRecurso'])),
            ('unidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Unidad'])),
        ))
        db.send_create_signal('sistema', ['Recurso'])

        # Adding model 'TipoCobro'
        db.create_table('sistema_tipocobro', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['TipoCobro'])

        # Adding model 'TipoObra'
        db.create_table('sistema_tipoobra', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['TipoObra'])

        # Adding model 'TipoEstado'
        db.create_table('sistema_tipoestado', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['TipoEstado'])

        # Adding model 'TipoChapa'
        db.create_table('sistema_tipochapa', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['TipoChapa'])

        # Adding model 'TipoEstructura1'
        db.create_table('sistema_tipoestructura1', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['TipoEstructura1'])

        # Adding model 'TipoEstructura2'
        db.create_table('sistema_tipoestructura2', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['TipoEstructura2'])

        # Adding model 'TipoTelefono'
        db.create_table('sistema_tipotelefono', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['TipoTelefono'])

        # Adding model 'Banco'
        db.create_table('sistema_banco', (
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=100, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sistema', ['Banco'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Pais'
        db.delete_table('sistema_pais')

        # Deleting model 'Provincia'
        db.delete_table('sistema_provincia')

        # Deleting model 'Ciudad'
        db.delete_table('sistema_ciudad')

        # Deleting model 'Titulo'
        db.delete_table('sistema_titulo')

        # Deleting model 'TipoRecurso'
        db.delete_table('sistema_tiporecurso')

        # Deleting model 'Unidad'
        db.delete_table('sistema_unidad')

        # Deleting model 'Recurso'
        db.delete_table('sistema_recurso')

        # Deleting model 'TipoCobro'
        db.delete_table('sistema_tipocobro')

        # Deleting model 'TipoObra'
        db.delete_table('sistema_tipoobra')

        # Deleting model 'TipoEstado'
        db.delete_table('sistema_tipoestado')

        # Deleting model 'TipoChapa'
        db.delete_table('sistema_tipochapa')

        # Deleting model 'TipoEstructura1'
        db.delete_table('sistema_tipoestructura1')

        # Deleting model 'TipoEstructura2'
        db.delete_table('sistema_tipoestructura2')

        # Deleting model 'TipoTelefono'
        db.delete_table('sistema_tipotelefono')

        # Deleting model 'Banco'
        db.delete_table('sistema_banco')
    
    
    models = {
        'sistema.banco': {
            'Meta': {'object_name': 'Banco'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Provincia']"})
        },
        'sistema.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.provincia': {
            'Meta': {'object_name': 'Provincia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Pais']"})
        },
        'sistema.recurso': {
            'Meta': {'object_name': 'Recurso'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recurso_tipo'", 'to': "orm['sistema.TipoRecurso']"}),
            'unidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Unidad']"})
        },
        'sistema.tipochapa': {
            'Meta': {'object_name': 'TipoChapa'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.tipocobro': {
            'Meta': {'object_name': 'TipoCobro'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.tipoestado': {
            'Meta': {'object_name': 'TipoEstado'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.tipoestructura1': {
            'Meta': {'object_name': 'TipoEstructura1'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.tipoestructura2': {
            'Meta': {'object_name': 'TipoEstructura2'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.tipoobra': {
            'Meta': {'object_name': 'TipoObra'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.tiporecurso': {
            'Meta': {'object_name': 'TipoRecurso'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.tipotelefono': {
            'Meta': {'object_name': 'TipoTelefono'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.titulo': {
            'Meta': {'object_name': 'Titulo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        'sistema.unidad': {
            'Meta': {'object_name': 'Unidad'},
            'abreviacion': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }
    
    complete_apps = ['sistema']
