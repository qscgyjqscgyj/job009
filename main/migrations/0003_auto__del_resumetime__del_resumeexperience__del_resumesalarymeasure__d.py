# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
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

        # Adding model 'AdEmployment'
        db.create_table(u'main_ademployment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['AdEmployment'])

        # Adding model 'AdExperience'
        db.create_table(u'main_adexperience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['AdExperience'])

        # Adding model 'AdSchedule'
        db.create_table(u'main_adschedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['AdSchedule'])

        # Adding model 'AdSalaryMeasure'
        db.create_table(u'main_adsalarymeasure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['AdSalaryMeasure'])

        # Adding model 'AdTime'
        db.create_table(u'main_adtime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['AdTime'])

        # Adding model 'AdCategory'
        db.create_table(u'main_adcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['AdCategory'])

        # Adding model 'AdArea'
        db.create_table(u'main_adarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'main', ['AdArea'])


    def backwards(self, orm):
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

        # Deleting model 'AdEmployment'
        db.delete_table(u'main_ademployment')

        # Deleting model 'AdExperience'
        db.delete_table(u'main_adexperience')

        # Deleting model 'AdSchedule'
        db.delete_table(u'main_adschedule')

        # Deleting model 'AdSalaryMeasure'
        db.delete_table(u'main_adsalarymeasure')

        # Deleting model 'AdTime'
        db.delete_table(u'main_adtime')

        # Deleting model 'AdCategory'
        db.delete_table(u'main_adcategory')

        # Deleting model 'AdArea'
        db.delete_table(u'main_adarea')


    models = {
        u'main.adarea': {
            'Meta': {'object_name': 'AdArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.adcategory': {
            'Meta': {'object_name': 'AdCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.ademployment': {
            'Meta': {'object_name': 'AdEmployment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.adexperience': {
            'Meta': {'object_name': 'AdExperience'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.adsalarymeasure': {
            'Meta': {'object_name': 'AdSalaryMeasure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.adschedule': {
            'Meta': {'object_name': 'AdSchedule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.adtime': {
            'Meta': {'object_name': 'AdTime'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']