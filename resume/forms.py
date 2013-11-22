# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django import forms
from main.models import AdSalaryMeasure, AdSubCategory, AdArea, Gender, MaritalStatus, City, AdCategory
from resume.models import Resume
from django.utils.translation import ugettext_lazy as _
from resume.widgets import ColumnCheckboxSelectMultiple


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
                                                 label=_(u'Специализация'), queryset=AdSubCategory.objects.all())
    marital_status = forms.ModelChoiceField(label=_(u'Семейное положение'), widget=forms.RadioSelect(),
                                            queryset=MaritalStatus.objects.all(), required=False)
    gender = forms.ModelChoiceField(label=_(u'Пол'), queryset=Gender.objects.all(), widget=forms.RadioSelect())
    city = forms.ModelChoiceField(queryset=City.objects.all(), label=_(u'Город проживания'),
                                  widget=forms.Select(attrs={'onchange': "Dajaxice.resume.city_area(Dajax.process, {'option':this.options[this.selectedIndex].innerHTML})",
                                                             'size': "1"}))
    category = forms.ModelChoiceField(queryset=AdCategory.objects.all(), label=_(u'Рубрика'),
                                      widget=forms.Select(attrs={'onchange': "Dajaxice.resume.category_subcategory(Dajax.process, {'option':this.options[this.selectedIndex].innerHTML})",
                                                                 'size': "1"}))
    photo = forms.ImageField(label=_(u'Фото'))

    def __init__(self,  *args, **kwargs):
        super(ResumeForm, self).__init__(*args, **kwargs)
        self.fields['salary_measure'].empty_label = None
        self.fields['city'].empty_label = None
        self.fields['area'].empty_label = None
        self.fields['marital_status'].empty_label = None
        self.fields['gender'].empty_label = None
        #self.fields['category'].empty_label = None

    class Meta:

        def __init__(self):
            pass

        model = Resume

        exclude = ('owner', 'date', 'rating', 'icq', 'skype', )


class ResumeAuthForm(forms.ModelForm):
    phone_details = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Доп. информация')}),
                                    label=_(u'Дополнительная информация'), required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': '_ad-email'}), label='E-mail')
    salary_measure = forms.ModelChoiceField(queryset=AdSalaryMeasure.objects.all(),
                                            widget=forms.Select(attrs={'class': '_ad_salary_measure'}))
    driving_license = forms.CheckboxInput()
    business_trip = forms.CheckboxInput()
    move = forms.BooleanField(widget=forms.RadioSelect(choices=((True, _(u'да')), (False, _(u'нет')))),
                              label=_(u'Переезд'), required=False)
    subcategory = forms.ModelMultipleChoiceField(widget=ColumnCheckboxSelectMultiple(columns=3),
                                                 label=_(u'Специализация'), queryset=AdSubCategory.objects.all())
    marital_status = forms.ModelChoiceField(label=_(u'Семейное положение'), widget=forms.RadioSelect(),
                                            queryset=MaritalStatus.objects.all(), required=False)
    gender = forms.ModelChoiceField(label=_(u'Пол'), queryset=Gender.objects.all(), widget=forms.RadioSelect())
    city = forms.ModelChoiceField(queryset=City.objects.all(), label=_(u'Город проживания'),
                                  widget=forms.Select(attrs={'onchange': "Dajaxice.resume.city_area(Dajax.process, {'option':this.options[this.selectedIndex].innerHTML})",
                                                             'size': "1"}))
    area = forms.ModelChoiceField(label=_(u'Район проживания'), queryset=AdArea.objects.all())
    category = forms.ModelChoiceField(queryset=AdCategory.objects.all(), label=_(u'Рубрика'),
                                      widget=forms.Select(attrs={'onchange': "Dajaxice.resume.category_subcategory(Dajax.process, {'option':this.options[this.selectedIndex].innerHTML})",
                                                                 'size': "1"}))
    photo = forms.ImageField(label=_(u'Фото'))

    def __init__(self,  *args, **kwargs):
        super(ResumeAuthForm, self).__init__(*args, **kwargs)
        self.fields['salary_measure'].empty_label = None
        self.fields['city'].empty_label = None
        self.fields['area'].empty_label = None
        self.fields['marital_status'].empty_label = None
        self.fields['gender'].empty_label = None
        #self.fields['category'].empty_label = None

    class Meta:

        def __init__(self):
            pass

        model = Resume

        exclude = ('owner', 'date', 'rating', 'icq', 'skype', )