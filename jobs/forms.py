# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms
from jobs.models import Job
from django.utils.translation import ugettext_lazy as _
from main.models import AdSubCategory, AdArea, City, AdCategory
from resume.widgets import ColumnCheckboxSelectMultiple


class JobForm(forms.ModelForm):
    street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Улица')}), label='Улица', required=False)
    building = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'№ дома')}), label='Здание',
                               required=False)
    about_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Дополнительно')}),
                                    label='Дополнительная информация', required=False)
    phone_details = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Доп. информация')}),
                                    label='Дополнительная информация', required=False)
    salary_from = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'от')}), label='Зарплата от',
                                  required=False)
    salary_to = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'до')}), label='Зарплата до',
                                required=False)
    #category = forms.ModelChoiceField(queryset=AdCategory.objects.all(), label=_(u'Сфера деятельности'),
    #                                  widget=forms.Select(attrs={'onchange': "Dajaxice.resume.category_subcategory(Dajax.process, {'option':this.options[this.selectedIndex].innerHTML})",
    #                                                             'size': "1"}))
    #subcategory = forms.ModelMultipleChoiceField(widget=ColumnCheckboxSelectMultiple(columns=3),
    #                                             label=_(u'Специализация'), queryset=AdSubCategory.objects.all())
    city = forms.ModelChoiceField(queryset=City.objects.all(), label=_(u'Город'),
                                  widget=forms.Select(attrs={'onchange': "Dajaxice.resume.city_area(Dajax.process, {'option':this.options[this.selectedIndex].innerHTML})",
                                                             'size': "1"}))
    area = forms.ModelChoiceField(label=_(u'Район'), queryset=AdArea.objects.all(), required=False)

    class Meta:

        def __init__(self):
            pass

        model = Job
        exclude = ('owner', 'subcategory', 'ad_time')