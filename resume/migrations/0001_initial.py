# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resume'
        db.create_table(u'resume_resume', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profile.CustomApplicant'], null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('office', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resume_category', to=orm['main.AdCategory'])),
            ('schedule', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_schedule', null=True, to=orm['main.AdSchedule'])),
            ('employment', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_employment', null=True, to=orm['main.AdEmployment'])),
            ('salary', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('salary_measure', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_salary_measure', null=True, to=orm['main.AdSalaryMeasure'])),
            ('fio', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('birth', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('gender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resume_gender', to=orm['main.Gender'])),
            ('marital_status', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_marital_status', null=True, to=orm['main.MaritalStatus'])),
            ('experience', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_experience', null=True, to=orm['main.AdExperience'])),
            ('skills', self.gf('django.db.models.fields.TextField')()),
            ('education', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resume_education', to=orm['main.Education'])),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('diploma', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('ex_education', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('qualities', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('driving_license', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('business_trip', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('file_resume', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resume_city', to=orm['main.City'])),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_area', null=True, to=orm['main.AdArea'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('phone_details', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('icq', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('move', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ad_time', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='resume_ad_time', null=True, to=orm['main.AdTime'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'resume', ['Resume'])

        # Adding M2M table for field subcategory on 'Resume'
        m2m_table_name = db.shorten_name(u'resume_resume_subcategory')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resume', models.ForeignKey(orm[u'resume.resume'], null=False)),
            ('adsubcategory', models.ForeignKey(orm[u'main.adsubcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['resume_id', 'adsubcategory_id'])

        # Adding M2M table for field work_area on 'Resume'
        m2m_table_name = db.shorten_name(u'resume_resume_work_area')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('resume', models.ForeignKey(orm[u'resume.resume'], null=False)),
            ('adarea', models.ForeignKey(orm[u'main.adarea'], null=False))
        ))
        db.create_unique(m2m_table_name, ['resume_id', 'adarea_id'])


    def backwards(self, orm):
        # Deleting model 'Resume'
        db.delete_table(u'resume_resume')

        # Removing M2M table for field subcategory on 'Resume'
        db.delete_table(db.shorten_name(u'resume_resume_subcategory'))

        # Removing M2M table for field work_area on 'Resume'
        db.delete_table(db.shorten_name(u'resume_resume_work_area'))


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
        u'main.education': {
            'Meta': {'object_name': 'Education'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        u'resume.resume': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Resume'},
            'ad_time': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_ad_time'", 'null': 'True', 'to': u"orm['main.AdTime']"}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_area'", 'null': 'True', 'to': u"orm['main.AdArea']"}),
            'birth': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'business_trip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resume_category'", 'to': u"orm['main.AdCategory']"}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resume_city'", 'to': u"orm['main.City']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'diploma': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'driving_license': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'education': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resume_education'", 'to': u"orm['main.Education']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'employment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_employment'", 'null': 'True', 'to': u"orm['main.AdEmployment']"}),
            'ex_education': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'experience': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_experience'", 'null': 'True', 'to': u"orm['main.AdExperience']"}),
            'file_resume': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resume_gender'", 'to': u"orm['main.Gender']"}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_marital_status'", 'null': 'True', 'to': u"orm['main.MaritalStatus']"}),
            'move': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'office': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user_profile.CustomApplicant']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone_details': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'qualities': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'salary_measure': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_salary_measure'", 'null': 'True', 'to': u"orm['main.AdSalaryMeasure']"}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'resume_schedule'", 'null': 'True', 'to': u"orm['main.AdSchedule']"}),
            'skills': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subcategory': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'resume_subcategory'", 'symmetrical': 'False', 'to': u"orm['main.AdSubCategory']"}),
            'work_area': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'resume_work_area'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['main.AdArea']"})
        },
        u'user_profile.customapplicant': {
            'Meta': {'object_name': 'CustomApplicant', '_ormbases': [u'auth.User']},
            'birth': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.City']", 'null': 'True', 'blank': 'True'}),
            'diploma': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'education': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'applicant_education'", 'null': 'True', 'to': u"orm['main.Education']"}),
            'ex_education': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'applicant_gender'", 'null': 'True', 'to': u"orm['main.Gender']"}),
            'icq': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'applicant_marital_status'", 'null': 'True', 'to': u"orm['main.MaritalStatus']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone_details': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['resume']