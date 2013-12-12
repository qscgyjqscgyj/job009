# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django import forms
from main.models import CompanyCategory, AdCategory
from resume.widgets import ColumnCheckboxSelectMultiple
from user_profile.models import CustomApplicant, CustomEmployer, CustomAgency
from django.utils.translation import ugettext_lazy as _


class CustomRegistrationForm(RegistrationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'id': '_reg-email'}), label='E-mail')
    username = forms.CharField(widget=forms.TextInput(attrs={'id': '_reg-username'}), label='Имя пользователя')
    captcha = CaptchaField()


class ApplicantProfileForm(forms.ModelForm):
    phone_details = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Дополнительная информация')}),
                                    label='Дополнительная информация', required=False)
    photo = forms.ImageField(label=_(u'Фото'), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'id': '_profile-username'}), label='Имя пользователя')

    class Meta:

        def __init__(self):
            pass

        model = CustomApplicant
        exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name',
                   'is_staff', 'is_active', 'date_joined', 'icq', 'skype', )


class EmployerProfileForm(forms.ModelForm):
    company_categories = forms.ModelMultipleChoiceField(required=False, widget=ColumnCheckboxSelectMultiple(columns=2),
                                                        label='Категория компании', queryset=AdCategory.objects.all().order_by('name'))
    street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Улица')}), label='Улица', required=False)
    building = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Здание')}), label='Здание',
                               required=False)
    about_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Дополнительная информация')}),
                                    label='Дополнительная информация', required=False)
    photo = forms.ImageField(label=_(u'Логотип'), required=False)

    def __init__(self,  *args, **kwargs):
        super(EmployerProfileForm, self).__init__(*args, **kwargs)
        self.fields['city'].empty_label = None

    class Meta:

        def __init__(self):
            pass

        model = CustomEmployer
        exclude = ('username', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name',
                   'last_name', 'is_staff', 'is_active', 'date_joined', 'captcha', )


class AgencyProfileForm(forms.ModelForm):
    company_categories = forms.ModelMultipleChoiceField(required=False, widget=ColumnCheckboxSelectMultiple(columns=2),
                                                        label='Категория компании', queryset=AdCategory.objects.all())
    street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Улица')}), label='Улица')
    building = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Здание')}), label='Здание')
    about_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Дополнительная информация')}),
                                    label='Дополнительная информация')

    class Meta:

        def __init__(self):
            pass

        model = CustomAgency
        exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name',
                   'is_staff', 'is_active', 'date_joined',)
