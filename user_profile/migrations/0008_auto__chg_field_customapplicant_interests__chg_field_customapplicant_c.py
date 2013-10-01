# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CustomApplicant.interests'
        db.alter_column(u'user_profile_customapplicant', 'interests', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CustomApplicant.city'
        db.alter_column(u'user_profile_customapplicant', 'city_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_geoip.City'], null=True))

        # Changing field 'CustomApplicant.gender'
        db.alter_column(u'user_profile_customapplicant', 'gender_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['user_profile.Gender']))

        # Changing field 'CustomApplicant.phone_details'
        db.alter_column(u'user_profile_customapplicant', 'phone_details', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'CustomApplicant.marital_status'
        db.alter_column(u'user_profile_customapplicant', 'marital_status_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['user_profile.MaritalStatus']))

        # Changing field 'CustomApplicant.professional_goals'
        db.alter_column(u'user_profile_customapplicant', 'professional_goals', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CustomApplicant.phone'
        db.alter_column(u'user_profile_customapplicant', 'phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'CustomApplicant.skype'
        db.alter_column(u'user_profile_customapplicant', 'skype', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'CustomApplicant.icq'
        db.alter_column(u'user_profile_customapplicant', 'icq', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'CustomApplicant.education'
        db.alter_column(u'user_profile_customapplicant', 'education_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['user_profile.Education']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'CustomApplicant.interests'
        raise RuntimeError("Cannot reverse this migration. 'CustomApplicant.interests' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CustomApplicant.interests'
        db.alter_column(u'user_profile_customapplicant', 'interests', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'CustomApplicant.city'
        raise RuntimeError("Cannot reverse this migration. 'CustomApplicant.city' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CustomApplicant.city'
        db.alter_column(u'user_profile_customapplicant', 'city_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_geoip.City']))

        # User chose to not deal with backwards NULL issues for 'CustomApplicant.gender'
        raise RuntimeError("Cannot reverse this migration. 'CustomApplicant.gender' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CustomApplicant.gender'
        db.alter_column(u'user_profile_customapplicant', 'gender_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profile.Gender']))

        # User chose to not deal with backwards NULL issues for 'CustomApplicant.phone_details'
        raise RuntimeError("Cannot reverse this migration. 'CustomApplicant.phone_details' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CustomApplicant.phone_details'
        db.alter_column(u'user_profile_customapplicant', 'phone_details', self.gf('django.db.models.fields.CharField')(max_length=100))

        # User chose to not deal with backwards NULL issues for 'CustomApplicant.marital_status'
        raise RuntimeError("Cannot reverse this migration. 'CustomApplicant.marital_status' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CustomApplicant.marital_status'
        db.alter_column(u'user_profile_customapplicant', 'marital_status_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profile.MaritalStatus']))

        # User chose to not deal with backwards NULL issues for 'CustomApplicant.professional_goals'
        raise RuntimeError("Cannot reverse this migration. 'CustomApplicant.professional_goals' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CustomApplicant.professional_goals'
        db.alter_column(u'user_profile_customapplicant', 'professional_goals', self.gf('django.db.models.fields.TextField')())

        # User chose to not deal with backwards NULL issues for 'CustomApplicant.phone'
        raise RuntimeError("Cannot reverse this migration. 'CustomApplicant.phone' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CustomApplicant.phone'
        db.alter_column(u'user_profile_customapplicant', 'phone', self.gf('django.db.models.fields.CharField')(max_length=100))

        # User chose to not deal with backwards NULL issues for 'CustomApplicant.skype'
        raise RuntimeError("Cannot reverse this migration. 'CustomApplicant.skype' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CustomApplicant.skype'
        db.alter_column(u'user_profile_customapplicant', 'skype', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'CustomApplicant.icq'
        raise RuntimeError("Cannot reverse this migration. 'CustomApplicant.icq' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CustomApplicant.icq'
        db.alter_column(u'user_profile_customapplicant', 'icq', self.gf('django.db.models.fields.CharField')(max_length=20))

        # User chose to not deal with backwards NULL issues for 'CustomApplicant.education'
        raise RuntimeError("Cannot reverse this migration. 'CustomApplicant.education' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'CustomApplicant.education'
        db.alter_column(u'user_profile_customapplicant', 'education_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profile.Education']))

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'django_geoip.city': {
            'Meta': {'unique_together': "(('region', 'name'),)", 'object_name': 'City'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cities'", 'to': u"orm['django_geoip.Region']"})
        },
        u'django_geoip.country': {
            'Meta': {'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'django_geoip.region': {
            'Meta': {'unique_together': "(('country', 'name'),)", 'object_name': 'Region'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'regions'", 'to': u"orm['django_geoip.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'user_profile.customagency': {
            'Meta': {'object_name': 'CustomAgency', '_ormbases': [u'auth.User']},
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'user_profile.customapplicant': {
            'Meta': {'object_name': 'CustomApplicant', '_ormbases': [u'auth.User']},
            'birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_geoip.City']", 'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'applicant_education'", 'null': 'True', 'to': u"orm['user_profile.Education']"}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'applicant_gender'", 'null': 'True', 'to': u"orm['user_profile.Gender']"}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'interests': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'applicant_marital_status'", 'null': 'True', 'to': u"orm['user_profile.MaritalStatus']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone_details': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'professional_goals': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'user_profile.customemployer': {
            'Meta': {'object_name': 'CustomEmployer', '_ormbases': [u'auth.User']},
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'user_profile.customlocation': {
            'Meta': {'object_name': 'CustomLocation'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'custom_location'", 'to': u"orm['django_geoip.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'user_profile.education': {
            'Meta': {'object_name': 'Education'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'user_profile.gender': {
            'Meta': {'object_name': 'Gender'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'user_profile.maritalstatus': {
            'Meta': {'object_name': 'MaritalStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['user_profile']