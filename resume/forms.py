# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms
from django_geoip.models import City, Region
from main.models import AdSalaryMeasure
from resume.models import Resume
from django.utils.translation import ugettext_lazy as _

CITIES = City.objects.all().filter(region=Region.objects.get(pk=80))
CHOICE_CITY = []
for CITY in CITIES:
    CHOICE_CITY.append((str(CITY).lower(), str(CITY).upper()))

DL_YES_NO = ((True, 'есть водительские права'))
BUSINESS_TRIP_YES_NO = ((True, 'готов к командировкам'), (False, 'не готов к командировкам'))
SMOKE_YES_NO = ((True, 'курю'), (False, 'не курю'))
MOVE_YES_NO = ((False, 'нет'), (None, 'возможен'), (True, 'обязателен'))


class ResumeForm(forms.ModelForm):
    phone_details = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Доп. информация')}),
                                    label='Дополнительная информация')
    move_cities = forms.MultipleChoiceField(required=False, choices=CHOICE_CITY,
                                            label=_(u'Возможные города для переезда'))
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': '_ad-email'}), label='E-mail')
    captcha = CaptchaField(label=_(u'Числовой код'))
    salary_measure = forms.ModelChoiceField(queryset=AdSalaryMeasure.objects.all())
    driving_license = forms.CheckboxInput()
    business_trip = forms.NullBooleanField(widget=forms.RadioSelect(choices=BUSINESS_TRIP_YES_NO))
    smoke = forms.NullBooleanField(widget=forms.RadioSelect(choices=SMOKE_YES_NO))
    move = forms.NullBooleanField(widget=forms.RadioSelect(choices=MOVE_YES_NO), label=_(u'Переезд'))

    def __init__(self, *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        model_choice_field = [field for salary_measure, field in self.fields.iteritems()
                              if isinstance(field, forms.ModelChoiceField)]

        for salary_measure in model_choice_field:
            salary_measure.empty_label = None

    class Meta:

        def __init__(self):
            pass

        model = Resume