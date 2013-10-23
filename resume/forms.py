# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms
from django_geoip.models import City, Region
from resume.models import Resume
from django.utils.translation import ugettext_lazy as _

CITIES = City.objects.all().filter(region=Region.objects.get(pk=80))
CHOICE_CITY = []
for CITY in CITIES:
    CHOICE_CITY.append((str(CITY).lower(), str(CITY).upper()))


class ResumeForm(forms.ModelForm):
    phone_details = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Доп. информация')}),
                                    label='Дополнительная информация')
    move_cities = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=CHOICE_CITY,
                                            label=_(u'Возможные города для переезда'))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': '_ad-email'}), label='E-mail')
    captcha = CaptchaField(label=_(u'Числовой код'))

    class Meta:

        def __init__(self):
            pass

        model = Resume