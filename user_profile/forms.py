# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django import forms
from main.models import CompanyCategory
from user_profile.models import CustomApplicant, CustomEmployer, CustomAgency
from django.utils.translation import ugettext_lazy as _

#добавление рубрик работодателя и кадровых агенств в массив для вывода в форме профиля
CHOICE_CATEGORIES = CompanyCategory.objects.all()
CHOICE_CATEGORY = []
for CATEGORY in CHOICE_CATEGORIES:
    CHOICE_CATEGORY.append((str(CATEGORY).lower(), str(CATEGORY).upper()))


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
    company_categories = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple,
                                                   choices=CHOICE_CATEGORY, label='Категория компании')
    street = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Улица')}), label='Улица')
    building = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Здание')}), label='Здание')
    about_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _(u'Дополнительная информация')}),
                                    label='Дополнительная информация')

    class Meta:

        def __init__(self):
            pass

        model = CustomEmployer
        exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name',
                   'is_staff', 'is_active', 'date_joined',)


class AgencyProfileForm(forms.ModelForm):
    company_categories = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple,
                                                   choices=CHOICE_CATEGORY, label='Категория компании')
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
