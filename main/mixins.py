# -*- coding: utf-8 -*-
from django.db import models
import pytils


def create_model(name, fields=None, app_label='', module='', options=None):
    """
    Create specified model
    """
    class Meta:
        # Using type('Meta', ...) gives a dictproxy error during model creation
        pass

    if app_label:
        # app_label must be set using the Meta inner class
        setattr(Meta, 'app_label', app_label)

    # Update Meta with any options that were provided
    if options is not None:
        for key, value in options.iteritems():
            setattr(Meta, key, value)

    # Set up a dictionary to simulate declarations within a class
    attrs = {'__module__': module, 'Meta': Meta}

    # Add in any fields that were provided
    if fields:
        attrs.update(fields)

    # Create the class, which automatically triggers ModelBase processing
    model = type(name, (models.Model,), attrs)

    return model


def SlugTraits(base_filed_name='name', slug_field_name='slug'):
    fields = {
        slug_field_name: models.SlugField(verbose_name=u'slug', max_length=150, blank=True, null=True)
    }
    SlugMixin = create_model('SlugMixin', fields=fields, module='main.models', options={'abstract': True})

    def save(self, **kwargs):
        original_text = getattr(self, base_filed_name)
        slug_text = pytils.translit.slugify(original_text)
        setattr(self, slug_field_name, slug_text)
        return super(SlugMixin, self).save(**kwargs)
    setattr(SlugMixin, 'save', save)
    return SlugMixin