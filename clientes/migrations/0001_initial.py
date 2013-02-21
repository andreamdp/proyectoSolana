# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Cliente'
        db.create_table('clientes_cliente', (
            ('provincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Provincia'], null=True, blank=True)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('cuit', self.gf('django.db.models.fields.PositiveIntegerField')(max_length=50, null=True, blank=True)),
            ('razon_social', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('cliente_nro', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Pais'], null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Ciudad'], null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Titulo'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('altura', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('clientes', ['Cliente'])

        # Adding model 'Telefono'
        db.create_table('clientes_telefono', (
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoTelefono'])),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
        ))
        db.send_create_signal('clientes', ['Telefono'])

        # Adding model 'Email'
        db.create_table('clientes_email', (
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(default='@', max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('clientes', ['Email'])

        # Adding model 'ConjuntoObra'
        db.create_table('clientes_conjuntoobra', (
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.Ciudad'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoEstado'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('director_obra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal('clientes', ['ConjuntoObra'])

        # Adding model 'Obra'
        db.create_table('clientes_obra', (
            ('cubierta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoEstructura1'], null=True, blank=True)),
            ('hierro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoEstructura2'], null=True, blank=True)),
            ('superficieChapa', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('perimetroBloque', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('bloque', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('largoCubierta', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('perimetroChapa', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('chapa', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('superficieCubierta', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('fieltro', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('observacion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('conjunto_obra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.ConjuntoObra'])),
            ('tipo_obra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoObra'])),
            ('porton', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('anchoCubierta', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('ancho', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('superficieBloque', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('superficie', self.gf('django.db.models.fields.FloatField')(default=0.0, blank=True)),
            ('largo', self.gf('django.db.models.fields.FloatField')(default=0.0, blank=True)),
            ('altoChapa', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
            ('canaletas', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('tipoChapa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoChapa'], null=True, blank=True)),
            ('altoBloque', self.gf('django.db.models.fields.FloatField')(default=0.0, null=True, blank=True)),
        ))
        db.send_create_signal('clientes', ['Obra'])

        # Adding model 'ConjuntoCosto'
        db.create_table('clientes_conjuntocosto', (
            ('obra', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['clientes.ConjuntoObra'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Cliente'])),
        ))
        db.send_create_signal('clientes', ['ConjuntoCosto'])

        # Adding model 'Costo'
        db.create_table('clientes_costo', (
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoRecurso'])),
            ('cantidad', self.gf('django.db.models.fields.DecimalField')(default=0.0, null=True, max_digits=5, decimal_places=2, blank=True)),
            ('conjunto_costo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.ConjuntoCosto'])),
            ('observaciones', self.gf('django.db.models.fields.TextField')(max_length=50, null=True, blank=True)),
            ('valor_unitario', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=5, decimal_places=2)),
            ('recurso', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['sistema.Recurso'])),
            ('total', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=10, decimal_places=2)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unidad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['sistema.Unidad'])),
        ))
        db.send_create_signal('clientes', ['Costo'])

        # Adding model 'Cobro'
        db.create_table('clientes_cobro', (
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_cobro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sistema.TipoCobro'])),
            ('observaciones', self.gf('django.db.models.fields.TextField')(max_length=50, null=True, blank=True)),
            ('conjunto_obra', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.ConjuntoObra'])),
            ('importe', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=7, decimal_places=2)),
        ))
        db.send_create_signal('clientes', ['Cobro'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Cliente'
        db.delete_table('clientes_cliente')

        # Deleting model 'Telefono'
        db.delete_table('clientes_telefono')

        # Deleting model 'Email'
        db.delete_table('clientes_email')

        # Deleting model 'ConjuntoObra'
        db.delete_table('clientes_conjuntoobra')

        # Deleting model 'Obra'
        db.delete_table('clientes_obra')

        # Deleting model 'ConjuntoCosto'
        db.delete_table('clientes_conjuntocosto')

        # Deleting model 'Costo'
        db.delete_table('clientes_costo')

        # Deleting model 'Cobro'
        db.delete_table('clientes_cobro')
    
    
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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 20, 9, 8, 48, 86574)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 20, 9, 8, 48, 86428)'}),
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
        'clientes.cobro': {
            'Meta': {'object_name': 'Cobro'},
            'conjunto_obra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.ConjuntoObra']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importe': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '7', 'decimal_places': '2'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tipo_cobro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.TipoCobro']"})
        },
        'clientes.conjuntocosto': {
            'Meta': {'object_name': 'ConjuntoCosto'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.Cliente']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obra': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['clientes.ConjuntoObra']"})
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
        'clientes.costo': {
            'Meta': {'object_name': 'Costo'},
            'cantidad': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'conjunto_costo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.ConjuntoCosto']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'recurso': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['sistema.Recurso']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.TipoRecurso']"}),
            'total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '10', 'decimal_places': '2'}),
            'unidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['sistema.Unidad']"}),
            'valor_unitario': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '5', 'decimal_places': '2'})
        },
        'clientes.email': {
            'Meta': {'object_name': 'Email'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.Cliente']"}),
            'email': ('django.db.models.fields.CharField', [], {'default': "'@'", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'clientes.obra': {
            'Meta': {'object_name': 'Obra'},
            'altoBloque': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'altoChapa': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'ancho': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'anchoCubierta': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'bloque': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'canaletas': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'chapa': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'conjunto_obra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.ConjuntoObra']"}),
            'cubierta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.TipoEstructura1']", 'null': 'True', 'blank': 'True'}),
            'fieltro': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'hierro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.TipoEstructura2']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'blank': 'True'}),
            'largoCubierta': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'observacion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'perimetroBloque': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'perimetroChapa': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'porton': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'superficie': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'blank': 'True'}),
            'superficieBloque': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'superficieChapa': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'superficieCubierta': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'tipoChapa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.TipoChapa']", 'null': 'True', 'blank': 'True'}),
            'tipo_obra': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.TipoObra']"})
        },
        'clientes.telefono': {
            'Meta': {'object_name': 'Telefono'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clientes.Cliente']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sistema.TipoTelefono']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
    
    complete_apps = ['clientes']
