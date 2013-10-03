# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ResumeTime'
        db.create_table(u'main_resumetime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['ResumeTime'])

        # Adding model 'ResumeExperience'
        db.create_table(u'main_resumeexperience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['ResumeExperience'])

        # Adding model 'ResumeSalaryMeasure'
        db.create_table(u'main_resumesalarymeasure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['ResumeSalaryMeasure'])

        # Adding model 'Area'
        db.create_table(u'main_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['Area'])

        # Adding model 'ResumeCategory'
        db.create_table(u'main_resumecategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['ResumeCategory'])

        # Adding model 'ResumeEmployment'
        db.create_table(u'main_resumeemployment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['ResumeEmployment'])

        # Adding model 'ResumeSchedule'
        db.create_table(u'main_resumeschedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['ResumeSchedule'])


    def backwards(self, orm):
        # Deleting model 'ResumeTime'
        db.delete_table(u'main_resumetime')

        # Deleting model 'ResumeExperience'
        db.delete_table(u'main_resumeexperience')

        # Deleting model 'ResumeSalaryMeasure'
        db.delete_table(u'main_resumesalarymeasure')

        # Deleting model 'Area'
        db.delete_table(u'main_area')

        # Deleting model 'ResumeCategory'
        db.delete_table(u'main_resumecategory')

        # Deleting model 'ResumeEmployment'
        db.delete_table(u'main_resumeemployment')

        # Deleting model 'ResumeSchedule'
        db.delete_table(u'main_resumeschedule')


    models = {
        u'main.area': {
            'Meta': {'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.resumecategory': {
            'Meta': {'object_name': 'ResumeCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.resumeemployment': {
            'Meta': {'object_name': 'ResumeEmployment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.resumeexperience': {
            'Meta': {'object_name': 'ResumeExperience'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.resumesalarymeasure': {
            'Meta': {'object_name': 'ResumeSalaryMeasure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.resumeschedule': {
            'Meta': {'object_name': 'ResumeSchedule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.resumetime': {
            'Meta': {'object_name': 'ResumeTime'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']