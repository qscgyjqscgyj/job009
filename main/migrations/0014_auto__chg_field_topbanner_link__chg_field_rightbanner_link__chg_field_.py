# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'TopBanner.link'
        db.alter_column(u'main_topbanner', 'link', self.gf('django.db.models.fields.URLField')(max_length=100, null=True))

        # Changing field 'RightBanner.link'
        db.alter_column(u'main_rightbanner', 'link', self.gf('django.db.models.fields.URLField')(max_length=100, null=True))

        # Changing field 'MiddleBanner.link'
        db.alter_column(u'main_middlebanner', 'link', self.gf('django.db.models.fields.URLField')(max_length=100, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'TopBanner.link'
        raise RuntimeError("Cannot reverse this migration. 'TopBanner.link' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'TopBanner.link'
        db.alter_column(u'main_topbanner', 'link', self.gf('django.db.models.fields.URLField')(max_length=100))

        # User chose to not deal with backwards NULL issues for 'RightBanner.link'
        raise RuntimeError("Cannot reverse this migration. 'RightBanner.link' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'RightBanner.link'
        db.alter_column(u'main_rightbanner', 'link', self.gf('django.db.models.fields.URLField')(max_length=100))

        # User chose to not deal with backwards NULL issues for 'MiddleBanner.link'
        raise RuntimeError("Cannot reverse this migration. 'MiddleBanner.link' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'MiddleBanner.link'
        db.alter_column(u'main_middlebanner', 'link', self.gf('django.db.models.fields.URLField')(max_length=100))

    models = {
        u'main.adarea': {
            'Meta': {'object_name': 'AdArea'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'areas'", 'to': u"orm['main.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.adcategory': {
            'Meta': {'object_name': 'AdCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
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
        u'main.adsubcategory': {
            'Meta': {'object_name': 'AdSubCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ad_sub_category_category'", 'to': u"orm['main.AdCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.adtime': {
            'Meta': {'object_name': 'AdTime'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.city': {
            'Meta': {'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.education': {
            'Meta': {'object_name': 'Education'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.employees': {
            'Meta': {'object_name': 'Employees'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.gender': {
            'Meta': {'object_name': 'Gender'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.maritalstatus': {
            'Meta': {'object_name': 'MaritalStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'main.middlebanner': {
            'Meta': {'object_name': 'MiddleBanner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'main.position': {
            'Meta': {'object_name': 'Position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.rightbanner': {
            'Meta': {'object_name': 'RightBanner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'main.topbanner': {
            'Meta': {'object_name': 'TopBanner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']