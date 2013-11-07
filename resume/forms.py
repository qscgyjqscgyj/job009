# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms
from django_geoip.models import City, Region
from main.models import AdSalaryMeasure, AdSubCategory, AdArea
from resume.models import Resume
from django.utils.translation import ugettext_lazy as _

CITIES = City.objects.all().filter(region=Region.objects.get(pk=80))
CHOICE_CITY = []
for CITY in CITIES:
    CHOICE_CITY.append((str(CITY).lower(), str(CITY).upper()))


class ResumeForm(forms.ModelForm):
    phone_details = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Доп. информация')}),
                                    label=_(u'Дополнительная информация'), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': '_ad-email'}), label='E-mail')
    captcha = CaptchaField(label=_(u'Числовой код'))
    salary_measure = forms.ModelChoiceField(queryset=AdSalaryMeasure.objects.all())
    driving_license = forms.CheckboxInput()
    business_trip = forms.CheckboxInput()
    move = forms.BooleanField(widget=forms.RadioSelect(choices=((True, _(u'да')), (False, _(u'нет')))),
                              label=_(u'Переезд'))
    subcategory = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                 queryset=AdSubCategory.objects.all(), label=_(u'Специализация'))
    work_area = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=AdArea.objects.all(),
                                               label=_(u'Желаемые районы для работы'))

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

        exclude = ('owner', 'date', 'rating', )