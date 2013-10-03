# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ResumeSalaryMeasure'
        db.create_table(u'resume_resumesalarymeasure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'resume', ['ResumeSalaryMeasure'])

        # Adding model 'Area'
        db.create_table(u'resume_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'resume', ['Area'])

        # Adding model 'Resume'
        db.create_table(u'resume_resume', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('office', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resume_category', to=orm['resume.ResumeCategory'])),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_schedule', null=True, to=orm['resume.ResumeSchedule'])),
            ('employment', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_employment', null=True, to=orm['resume.ResumeEmployment'])),
            ('salary', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('salary_measure', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_salary_measure', null=True, to=orm['resume.ResumeSalaryMeasure'])),
            ('fio', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('birth', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resume_gender', to=orm['user_profile.Gender'])),
            ('marital_status', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_marital_status', null=True, to=orm['user_profile.MaritalStatus'])),
            ('experience', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_experience', null=True, to=orm['resume.ResumeExperience'])),
            ('skills', self.gf('django.db.models.fields.TextField')()),
            ('education', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resume_education', to=orm['user_profile.Education'])),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('diploma', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('ex_education', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('qualities', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('driving_license', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('business_trip', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('smoke', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('file_resume', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resume_city', to=orm['django_geoip.City'])),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_area', null=True, to=orm['resume.Area'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phone_details', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('icq', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('move', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('ad_time', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_ad_time', null=True, to=orm['resume.ResumeTime'])),
        ))
        db.send_create_signal(u'resume', ['Resume'])

        # Adding M2M table for field work_area on 'Resume'
        m2m_table_name = db.shorten_name(u'resume_resume_work_area')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resume', models.ForeignKey(orm[u'resume.resume'], null=False)),
            ('area', models.ForeignKey(orm[u'resume.area'], null=False))
        ))
        db.create_unique(m2m_table_name, ['resume_id', 'area_id'])

        # Adding M2M table for field move_cities on 'Resume'
        m2m_table_name = db.shorten_name(u'resume_resume_move_cities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resume', models.ForeignKey(orm[u'resume.resume'], null=False)),
            ('city', models.ForeignKey(orm[u'django_geoip.city'], null=False))
        ))
        db.create_unique(m2m_table_name, ['resume_id', 'city_id'])

        # Adding model 'ResumeSchedule'
        db.create_table(u'resume_resumeschedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'resume', ['ResumeSchedule'])

        # Adding model 'ResumeExperience'
        db.create_table(u'resume_resumeexperience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'resume', ['ResumeExperience'])

        # Adding model 'ResumeCategory'
        db.create_table(u'resume_resumecategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'resume', ['ResumeCategory'])

        # Adding model 'ResumeEmployment'
        db.create_table(u'resume_resumeemployment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'resume', ['ResumeEmployment'])

        # Adding model 'ResumeTime'
        db.create_table(u'resume_resumetime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'resume', ['ResumeTime'])


    def backwards(self, orm):
        # Deleting model 'ResumeSalaryMeasure'
        db.delete_table(u'resume_resumesalarymeasure')

        # Deleting model 'Area'
        db.delete_table(u'resume_area')

        # Deleting model 'Resume'
        db.delete_table(u'resume_resume')

        # Removing M2M table for field work_area on 'Resume'
        db.delete_table(db.shorten_name(u'resume_resume_work_area'))

        # Removing M2M table for field move_cities on 'Resume'
        db.delete_table(db.shorten_name(u'resume_resume_move_cities'))

        # Deleting model 'ResumeSchedule'
        db.delete_table(u'resume_resumeschedule')

        # Deleting model 'ResumeExperience'
        db.delete_table(u'resume_resumeexperience')

        # Deleting model 'ResumeCategory'
        db.delete_table(u'resume_resumecategory')

        # Deleting model 'ResumeEmployment'
        db.delete_table(u'resume_resumeemployment')

        # Deleting model 'ResumeTime'
        db.delete_table(u'resume_resumetime')


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
        u'resume.area': {
            'Meta': {'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'resume.resume': {
            'Meta': {'object_name': 'Resume'},
            'ad_time': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_ad_time'", 'null': 'True', 'to': u"orm['resume.ResumeTime']"}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_area'", 'null': 'True', 'to': u"orm['resume.Area']"}),
            'birth': ('django.db.models.fields.DateField', [], {}),
            'business_trip': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resume_category'", 'to': u"orm['resume.ResumeCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resume_city'", 'to': u"orm['django_geoip.City']"}),
            'diploma': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'driving_license': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resume_education'", 'to': u"orm['user_profile.Education']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'employment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_employment'", 'null': 'True', 'to': u"orm['resume.ResumeEmployment']"}),
            'ex_education': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'experience': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_experience'", 'null': 'True', 'to': u"orm['resume.ResumeExperience']"}),
            'file_resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resume_gender'", 'to': u"orm['user_profile.Gender']"}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_marital_status'", 'null': 'True', 'to': u"orm['user_profile.MaritalStatus']"}),
            'move': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'move_cities': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['django_geoip.City']", 'null': 'True', 'blank': 'True'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone_details': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'qualities': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'salary_measure': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_salary_measure'", 'null': 'True', 'to': u"orm['resume.ResumeSalaryMeasure']"}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_schedule'", 'null': 'True', 'to': u"orm['resume.ResumeSchedule']"}),
            'skills': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'smoke': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'work_area': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'resume_work_area'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['resume.Area']"})
        },
        u'resume.resumecategory': {
            'Meta': {'object_name': 'ResumeCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'resume.resumeemployment': {
            'Meta': {'object_name': 'ResumeEmployment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'resume.resumeexperience': {
            'Meta': {'object_name': 'ResumeExperience'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'resume.resumesalarymeasure': {
            'Meta': {'object_name': 'ResumeSalaryMeasure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'resume.resumeschedule': {
            'Meta': {'object_name': 'ResumeSchedule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'resume.resumetime': {
            'Meta': {'object_name': 'ResumeTime'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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

    complete_apps = ['resume']