# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Knowledge'
        db.delete_table(u'umkm_knowledge')

        # Removing M2M table for field files on 'Knowledge'
        db.delete_table(db.shorten_name(u'umkm_knowledge_files'))

        # Removing M2M table for field tags on 'Knowledge'
        db.delete_table(db.shorten_name(u'umkm_knowledge_tags'))

        # Deleting model 'Category'
        db.delete_table(u'umkm_category')

        # Deleting model 'Media'
        db.delete_table(u'umkm_media')

        # Deleting model 'Type'
        db.delete_table(u'umkm_type')

        # Deleting model 'Tag'
        db.delete_table(u'umkm_tag')

        # Deleting model 'Relationship'
        db.delete_table(u'umkm_relationship')


    def backwards(self, orm):
        # Adding model 'Knowledge'
        db.create_table(u'umkm_knowledge', (
            ('status', self.gf('django.db.models.fields.BooleanField')()),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('post_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['umkm.Category'])),
            ('post_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['umkm.Type'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('post_content', self.gf('django.db.models.fields.TextField')()),
            ('post_excerpt', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'umkm', ['Knowledge'])

        # Adding M2M table for field files on 'Knowledge'
        m2m_table_name = db.shorten_name(u'umkm_knowledge_files')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('knowledge', models.ForeignKey(orm[u'umkm.knowledge'], null=False)),
            ('media', models.ForeignKey(orm[u'umkm.media'], null=False))
        ))
        db.create_unique(m2m_table_name, ['knowledge_id', 'media_id'])

        # Adding M2M table for field tags on 'Knowledge'
        m2m_table_name = db.shorten_name(u'umkm_knowledge_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('knowledge', models.ForeignKey(orm[u'umkm.knowledge'], null=False)),
            ('tag', models.ForeignKey(orm[u'umkm.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['knowledge_id', 'tag_id'])

        # Adding model 'Category'
        db.create_table(u'umkm_category', (
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['umkm.Category'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'umkm', ['Category'])

        # Adding model 'Media'
        db.create_table(u'umkm_media', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('shareable', self.gf('django.db.models.fields.BooleanField')()),
            ('media_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['umkm.Type'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'umkm', ['Media'])

        # Adding model 'Type'
        db.create_table(u'umkm_type', (
            ('type_for', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'umkm', ['Type'])

        # Adding model 'Tag'
        db.create_table(u'umkm_tag', (
            ('tag_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'umkm', ['Tag'])

        # Adding model 'Relationship'
        db.create_table(u'umkm_relationship', (
            ('to_knowledge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to', to=orm['umkm.Knowledge'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('relation_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['umkm.Type'])),
            ('from_knowledge', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from', to=orm['umkm.Knowledge'])),
        ))
        db.send_create_signal(u'umkm', ['Relationship'])


    models = {
        
    }

    complete_apps = ['umkm']