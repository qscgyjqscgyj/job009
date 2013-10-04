# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms
from jobs.models import Job
from django.utils.translation import ugettext_lazy as _


class JobForm(forms.ModelForm):
    street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Улица')}), label='Улица')
    building = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Здание')}), label='Здание')
    about_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Доп. информация')}),
                                    label='Дополнительная информация')
    phone_details = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Доп. информация')}),
                                    label='Дополнительная информация')
    captcha = CaptchaField()

    class Meta:

        def __init__(self):
            pass

        model = Job