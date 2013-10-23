# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Job'
        db.create_table(u'jobs_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('office', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_category', to=orm['main.AdCategory'])),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='job_schedule', null=True, to=orm['main.AdSchedule'])),
            ('employment', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='job_employment', null=True, to=orm['main.AdEmployment'])),
            ('salary_from', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('salary_to', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('salary_measure', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='job_salary_measure', null=True, to=orm['main.AdSalaryMeasure'])),
            ('about_job', self.gf('django.db.models.fields.TextField')()),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='job_city', to=orm['django_geoip.City'])),
            ('another_city_candidate', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('about_address', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('education', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='job_education', null=True, to=orm['main.Education'])),
            ('experience', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='job_experience', null=True, to=orm['main.AdExperience'])),
            ('skills', self.gf('django.db.models.fields.TextField')()),
            ('driving_license', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('business_trip', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('smoke', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='job_area', null=True, to=orm['main.AdArea'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone_details', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('icq', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('move', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('ad_time', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='job_ad_time', null=True, to=orm['main.AdTime'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'jobs', ['Job'])

        # Adding M2M table for field move_cities on 'Job'
        m2m_table_name = db.shorten_name(u'jobs_job_move_cities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('job', models.ForeignKey(orm[u'jobs.job'], null=False)),
            ('city', models.ForeignKey(orm[u'django_geoip.city'], null=False))
        ))
        db.create_unique(m2m_table_name, ['job_id', 'city_id'])


    def backwards(self, orm):
        # Deleting model 'Job'
        db.delete_table(u'jobs_job')

        # Removing M2M table for field move_cities on 'Job'
        db.delete_table(db.shorten_name(u'jobs_job_move_cities'))


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
        u'jobs.job': {
            'Meta': {'object_name': 'Job'},
            'about_address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'about_job': ('django.db.models.fields.TextField', [], {}),
            'ad_time': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job_ad_time'", 'null': 'True', 'to': u"orm['main.AdTime']"}),
            'another_city_candidate': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job_area'", 'null': 'True', 'to': u"orm['main.AdArea']"}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'business_trip': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_category'", 'to': u"orm['main.AdCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'job_city'", 'to': u"orm['django_geoip.City']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'driving_license': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job_education'", 'null': 'True', 'to': u"orm['main.Education']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'employment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job_employment'", 'null': 'True', 'to': u"orm['main.AdEmployment']"}),
            'experience': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job_experience'", 'null': 'True', 'to': u"orm['main.AdExperience']"}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'move': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'move_cities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['django_geoip.City']", 'null': 'True', 'blank': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_details': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'salary_from': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'salary_measure': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job_salary_measure'", 'null': 'True', 'to': u"orm['main.AdSalaryMeasure']"}),
            'salary_to': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job_schedule'", 'null': 'True', 'to': u"orm['main.AdSchedule']"}),
            'skills': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'smoke': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'main.adarea': {
            'Meta': {'object_name': 'AdArea'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'areas'", 'to': u"orm['django_geoip.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.adcategory': {
            'Meta': {'object_name': 'AdCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subcategory': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'ad_category_subcategory'", 'symmetrical': 'False', 'to': u"orm['main.AdSubCategory']"})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.adtime': {
            'Meta': {'object_name': 'AdTime'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'main.education': {
            'Meta': {'object_name': 'Education'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['jobs']