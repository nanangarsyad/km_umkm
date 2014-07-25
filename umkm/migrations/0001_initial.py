# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Type'
        db.create_table(u'umkm_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type_for', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'umkm', ['Type'])

        # Adding model 'Category'
        db.create_table(u'umkm_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['umkm.Category'])),
        ))
        db.send_create_signal(u'umkm', ['Category'])

        # Adding model 'Tag'
        db.create_table(u'umkm_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'umkm', ['Tag'])

        # Adding model 'Media'
        db.create_table(u'umkm_media', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('media_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['umkm.Type'])),
        ))
        db.send_create_signal(u'umkm', ['Media'])

        # Adding model 'Knowledge'
        db.create_table(u'umkm_knowledge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('post_content', self.gf('django.db.models.fields.TextField')()),
            ('post_excerpt', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.BooleanField')()),
            ('post_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['umkm.Type'])),
            ('post_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['umkm.Category'])),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'umkm', ['Knowledge'])

        # Adding M2M table for field tags on 'Knowledge'
        m2m_table_name = db.shorten_name(u'umkm_knowledge_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('knowledge', models.ForeignKey(orm[u'umkm.knowledge'], null=False)),
            ('tag', models.ForeignKey(orm[u'umkm.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['knowledge_id', 'tag_id'])

        # Adding M2M table for field files on 'Knowledge'
        m2m_table_name = db.shorten_name(u'umkm_knowledge_files')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('knowledge', models.ForeignKey(orm[u'umkm.knowledge'], null=False)),
            ('media', models.ForeignKey(orm[u'umkm.media'], null=False))
        ))
        db.create_unique(m2m_table_name, ['knowledge_id', 'media_id'])

        # Adding model 'Relationship'
        db.create_table(u'umkm_relationship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_knowledge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from', to=orm['umkm.Knowledge'])),
            ('to_knowledge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to', to=orm['umkm.Knowledge'])),
            ('relation_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['umkm.Type'])),
        ))
        db.send_create_signal(u'umkm', ['Relationship'])


    def backwards(self, orm):
        # Deleting model 'Type'
        db.delete_table(u'umkm_type')

        # Deleting model 'Category'
        db.delete_table(u'umkm_category')

        # Deleting model 'Tag'
        db.delete_table(u'umkm_tag')

        # Deleting model 'Media'
        db.delete_table(u'umkm_media')

        # Deleting model 'Knowledge'
        db.delete_table(u'umkm_knowledge')

        # Removing M2M table for field tags on 'Knowledge'
        db.delete_table(db.shorten_name(u'umkm_knowledge_tags'))

        # Removing M2M table for field files on 'Knowledge'
        db.delete_table(db.shorten_name(u'umkm_knowledge_files'))

        # Deleting model 'Relationship'
        db.delete_table(u'umkm_relationship')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'umkm.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['umkm.Category']"})
        },
        u'umkm.knowledge': {
            'Meta': {'object_name': 'Knowledge'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['umkm.Media']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['umkm.Category']"}),
            'post_content': ('django.db.models.fields.TextField', [], {}),
            'post_excerpt': ('django.db.models.fields.TextField', [], {}),
            'post_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['umkm.Type']"}),
            'relationsip': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_to'", 'symmetrical': 'False', 'through': u"orm['umkm.Relationship']", 'to': u"orm['umkm.Knowledge']"}),
            'status': ('django.db.models.fields.BooleanField', [], {}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['umkm.Tag']", 'symmetrical': 'False'})
        },
        u'umkm.media': {
            'Meta': {'object_name': 'Media'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['umkm.Type']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'umkm.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'from_knowledge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from'", 'to': u"orm['umkm.Knowledge']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relation_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['umkm.Type']"}),
            'to_knowledge': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to'", 'to': u"orm['umkm.Knowledge']"})
        },
        u'umkm.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'umkm.type': {
            'Meta': {'object_name': 'Type'},
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type_for': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['umkm']