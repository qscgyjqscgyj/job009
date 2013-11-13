# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms
from django_geoip.models import City, Region
from main.models import AdSalaryMeasure, AdSubCategory, AdArea, Gender, MaritalStatus
from resume.models import Resume
from django.utils.translation import ugettext_lazy as _
from resume.widgets import ColumnCheckboxSelectMultiple


def choice_city():
    cities = City.objects.all().filter(region=Region.objects.get(pk=80))
    choice = []
    for CITY in cities:
        c = City.objects.get(pk=CITY.pk)
        choice.append((c.pk, c))
    for CITY in cities:
        if CITY == City.objects.get(pk=1428):
            c = City.objects.get(pk=CITY.pk)
            choice[0] = (c.pk, c)
    return choice


class ResumeForm(forms.ModelForm):
    phone_details = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Доп. информация')}),
                                    label=_(u'Дополнительная информация'), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': '_ad-email'}), label='E-mail')
    captcha = CaptchaField(label=_(u'Числовой код'))
    salary_measure = forms.ModelChoiceField(queryset=AdSalaryMeasure.objects.all(),
                                            widget=forms.Select(attrs={'class': '_ad_salary_measure'}))
    driving_license = forms.CheckboxInput()
    business_trip = forms.CheckboxInput()
    move = forms.BooleanField(widget=forms.RadioSelect(choices=((True, _(u'да')), (False, _(u'нет')))),
                              label=_(u'Переезд'), required=False)
    subcategory = forms.ModelMultipleChoiceField(widget=ColumnCheckboxSelectMultiple(columns=3),
                                                 queryset=AdSubCategory.objects.all(), label=_(u'Специализация'))
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(),
                                    widget=forms.Select(attrs={'onchange': "Dajaxice.resume.gender_marital(Dajax.process, {'option':this.options[this.selectedIndex].innerHTML})",
                                                               'size': "1"}), label=_(u'Пол'))
    marital_status = forms.ModelChoiceField(queryset=MaritalStatus.objects.filter(gender=1),
                                            label=_(u'Семейное положение'))
    city = forms.ChoiceField(choices=choice_city(), label=_(u'Город проживания'))

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

        exclude = ('owner', 'date', 'rating', 'icq', 'skype', )