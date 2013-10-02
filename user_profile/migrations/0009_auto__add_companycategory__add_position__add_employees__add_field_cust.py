# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CompanyCategory'
        db.create_table(u'user_profile_companycategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'user_profile', ['CompanyCategory'])

        # Adding model 'Position'
        db.create_table(u'user_profile_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'user_profile', ['Position'])

        # Adding model 'Employees'
        db.create_table(u'user_profile_employees', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'user_profile', ['Employees'])

        # Adding field 'CustomAgency.contact'
        db.add_column(u'user_profile_customagency', 'contact',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomAgency.position'
        db.add_column(u'user_profile_customagency', 'position',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='add_employer_position', null=True, to=orm['user_profile.Position']),
                      keep_default=False)

        # Adding field 'CustomAgency.phone'
        db.add_column(u'user_profile_customagency', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomAgency.company_name'
        db.add_column(u'user_profile_customagency', 'company_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomAgency.legal_company_name'
        db.add_column(u'user_profile_customagency', 'legal_company_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomAgency.photo'
        db.add_column(u'user_profile_customagency', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomAgency.site'
        db.add_column(u'user_profile_customagency', 'site',
                      self.gf('django.db.models.fields.URLField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomAgency.employees'
        db.add_column(u'user_profile_customagency', 'employees',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='add_number_of_employees', null=True, to=orm['user_profile.Employees']),
                      keep_default=False)

        # Adding field 'CustomAgency.city'
        db.add_column(u'user_profile_customagency', 'city',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_geoip.City'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomAgency.street'
        db.add_column(u'user_profile_customagency', 'street',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomAgency.building'
        db.add_column(u'user_profile_customagency', 'building',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomAgency.about_address'
        db.add_column(u'user_profile_customagency', 'about_address',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field company_categories on 'CustomAgency'
        m2m_table_name = db.shorten_name(u'user_profile_customagency_company_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customagency', models.ForeignKey(orm[u'user_profile.customagency'], null=False)),
            ('companycategory', models.ForeignKey(orm[u'user_profile.companycategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customagency_id', 'companycategory_id'])

        # Adding field 'CustomEmployer.contact'
        db.add_column(u'user_profile_customemployer', 'contact',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomEmployer.position'
        db.add_column(u'user_profile_customemployer', 'position',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='position', null=True, to=orm['user_profile.Position']),
                      keep_default=False)

        # Adding field 'CustomEmployer.phone'
        db.add_column(u'user_profile_customemployer', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomEmployer.company_name'
        db.add_column(u'user_profile_customemployer', 'company_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomEmployer.legal_company_name'
        db.add_column(u'user_profile_customemployer', 'legal_company_name',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomEmployer.photo'
        db.add_column(u'user_profile_customemployer', 'photo',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomEmployer.site'
        db.add_column(u'user_profile_customemployer', 'site',
                      self.gf('django.db.models.fields.URLField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomEmployer.employees'
        db.add_column(u'user_profile_customemployer', 'employees',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='employees', null=True, to=orm['user_profile.Employees']),
                      keep_default=False)

        # Adding field 'CustomEmployer.city'
        db.add_column(u'user_profile_customemployer', 'city',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_geoip.City'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomEmployer.street'
        db.add_column(u'user_profile_customemployer', 'street',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomEmployer.building'
        db.add_column(u'user_profile_customemployer', 'building',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CustomEmployer.about_address'
        db.add_column(u'user_profile_customemployer', 'about_address',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field company_categories on 'CustomEmployer'
        m2m_table_name = db.shorten_name(u'user_profile_customemployer_company_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customemployer', models.ForeignKey(orm[u'user_profile.customemployer'], null=False)),
            ('companycategory', models.ForeignKey(orm[u'user_profile.companycategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['customemployer_id', 'companycategory_id'])


    def backwards(self, orm):
        # Deleting model 'CompanyCategory'
        db.delete_table(u'user_profile_companycategory')

        # Deleting model 'Position'
        db.delete_table(u'user_profile_position')

        # Deleting model 'Employees'
        db.delete_table(u'user_profile_employees')

        # Deleting field 'CustomAgency.contact'
        db.delete_column(u'user_profile_customagency', 'contact')

        # Deleting field 'CustomAgency.position'
        db.delete_column(u'user_profile_customagency', 'position_id')

        # Deleting field 'CustomAgency.phone'
        db.delete_column(u'user_profile_customagency', 'phone')

        # Deleting field 'CustomAgency.company_name'
        db.delete_column(u'user_profile_customagency', 'company_name')

        # Deleting field 'CustomAgency.legal_company_name'
        db.delete_column(u'user_profile_customagency', 'legal_company_name')

        # Deleting field 'CustomAgency.photo'
        db.delete_column(u'user_profile_customagency', 'photo')

        # Deleting field 'CustomAgency.site'
        db.delete_column(u'user_profile_customagency', 'site')

        # Deleting field 'CustomAgency.employees'
        db.delete_column(u'user_profile_customagency', 'employees_id')

        # Deleting field 'CustomAgency.city'
        db.delete_column(u'user_profile_customagency', 'city_id')

        # Deleting field 'CustomAgency.street'
        db.delete_column(u'user_profile_customagency', 'street')

        # Deleting field 'CustomAgency.building'
        db.delete_column(u'user_profile_customagency', 'building')

        # Deleting field 'CustomAgency.about_address'
        db.delete_column(u'user_profile_customagency', 'about_address')

        # Removing M2M table for field company_categories on 'CustomAgency'
        db.delete_table(db.shorten_name(u'user_profile_customagency_company_categories'))

        # Deleting field 'CustomEmployer.contact'
        db.delete_column(u'user_profile_customemployer', 'contact')

        # Deleting field 'CustomEmployer.position'
        db.delete_column(u'user_profile_customemployer', 'position_id')

        # Deleting field 'CustomEmployer.phone'
        db.delete_column(u'user_profile_customemployer', 'phone')

        # Deleting field 'CustomEmployer.company_name'
        db.delete_column(u'user_profile_customemployer', 'company_name')

        # Deleting field 'CustomEmployer.legal_company_name'
        db.delete_column(u'user_profile_customemployer', 'legal_company_name')

        # Deleting field 'CustomEmployer.photo'
        db.delete_column(u'user_profile_customemployer', 'photo')

        # Deleting field 'CustomEmployer.site'
        db.delete_column(u'user_profile_customemployer', 'site')

        # Deleting field 'CustomEmployer.employees'
        db.delete_column(u'user_profile_customemployer', 'employees_id')

        # Deleting field 'CustomEmployer.city'
        db.delete_column(u'user_profile_customemployer', 'city_id')

        # Deleting field 'CustomEmployer.street'
        db.delete_column(u'user_profile_customemployer', 'street')

        # Deleting field 'CustomEmployer.building'
        db.delete_column(u'user_profile_customemployer', 'building')

        # Deleting field 'CustomEmployer.about_address'
        db.delete_column(u'user_profile_customemployer', 'about_address')

        # Removing M2M table for field company_categories on 'CustomEmployer'
        db.delete_table(db.shorten_name(u'user_profile_customemployer_company_categories'))


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
        u'user_profile.companycategory': {
            'Meta': {'object_name': 'CompanyCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'user_profile.customagency': {
            'Meta': {'object_name': 'CustomAgency', '_ormbases': [u'auth.User']},
            'about_address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_geoip.City']", 'null': 'True', 'blank': 'True'}),
            'company_categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'add_employer_company_categories'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['user_profile.CompanyCategory']"}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'employees': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'add_number_of_employees'", 'null': 'True', 'to': u"orm['user_profile.Employees']"}),
            'legal_company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'add_employer_position'", 'null': 'True', 'to': u"orm['user_profile.Position']"}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'about_address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'building': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_geoip.City']", 'null': 'True', 'blank': 'True'}),
            'company_categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'company_categories'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['user_profile.CompanyCategory']"}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'employees': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'employees'", 'null': 'True', 'to': u"orm['user_profile.Employees']"}),
            'legal_company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'position'", 'null': 'True', 'to': u"orm['user_profile.Position']"}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
        u'user_profile.employees': {
            'Meta': {'object_name': 'Employees'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
        },
        u'user_profile.position': {
            'Meta': {'object_name': 'Position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['user_profile']