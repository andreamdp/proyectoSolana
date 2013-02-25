# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Categoria'
        db.create_table('pruebas_categoria', (
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('pruebas', ['Categoria'])

        # Adding model 'SubCategoria'
        db.create_table('pruebas_subcategoria', (
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['pruebas.Categoria'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('pruebas', ['SubCategoria'])

        # Adding model 'Presupuesto'
        db.create_table('pruebas_presupuesto', (
            ('obra', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['clientes.ConjuntoObra'])),
            ('total', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
        ))
        db.send_create_signal('pruebas', ['Presupuesto'])

        # Adding model 'Detalle'
        db.create_table('pruebas_detalle', (
            ('categoria', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['pruebas.Categoria'])),
            ('concepto', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['pruebas.SubCategoria'])),
            ('precio', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('presupuesto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pruebas.Presupuesto'])),
        ))
        db.send_create_signal('pruebas', ['Detalle'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Categoria'
        db.delete_table('pruebas_categoria')

        # Deleting model 'SubCategoria'
        db.delete_table('pruebas_subcategoria')

        # Deleting model 'Presupuesto'
        db.delete_table('pruebas_presupuesto')

        # Deleting model 'Detalle'
        db.delete_table('pruebas_detalle')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 14, 58, 49, 510653)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 14, 58, 49, 510501)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'altura': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Ciudad']", 'null': 'True', 'blank': 'True'}),
            'cliente_nro': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cuit': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Pais']", 'null': 'True', 'blank': 'True'}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Provincia']", 'null': 'True', 'blank': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Titulo']", 'null': 'True', 'blank': 'True'})
        },
        'clientes.conjuntoobra': {
            'Meta': {'object_name': 'ConjuntoObra'},
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.Ciudad']"}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.Cliente']"}),
            'director_obra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.TipoEstado']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pruebas.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'pruebas.detalle': {
            'Meta': {'object_name': 'Detalle'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['pruebas.Categoria']"}),
            'concepto': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['pruebas.SubCategoria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'presupuesto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pruebas.Presupuesto']"})
        },
        'pruebas.presupuesto': {
            'Meta': {'object_name': 'Presupuesto'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.Cliente']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obra': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['clientes.ConjuntoObra']"}),
            'total': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'pruebas.subcategoria': {
            'Meta': {'object_name': 'SubCategoria'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['pruebas.Categoria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '25'})
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
        'sistema.tipoestado': {
            'Meta': {'object_name': 'TipoEstado'},
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sistema.titulo': {
            'Meta': {'object_name': 'Titulo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }
    
    complete_apps = ['pruebas']
