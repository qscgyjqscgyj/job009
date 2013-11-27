# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms
from django_geoip.models import City, Region
from jobs.models import Job
from django.utils.translation import ugettext_lazy as _


class JobForm(forms.ModelForm):
    street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Улица')}), label='Улица')
    building = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Здание')}), label='Здание')
    about_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Доп. информация')}),
                                    label='Дополнительная информация')
    phone_details = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Доп. информация')}),
                                    label='Дополнительная информация')
    salary_from = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'от')}), label='Зарплата от')
    salary_to = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'до')}), label='Зарплата до')
    #move_cities = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=CHOICE_CITY)

    captcha = CaptchaField()

    class Meta:

        def __init__(self):
            pass

        model = Job