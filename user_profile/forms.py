# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django import forms
from user_profile.models import CustomApplicant, CustomEmployer, CustomAgency


class CustomRegistrationForm(RegistrationForm):
    captcha = CaptchaField()


class ApplicantProfileForm(forms.ModelForm):

    class Meta:

        def __init__(self):
            pass

        model = CustomApplicant
        exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name',
                   'is_staff', 'is_active', 'date_joined',)


class EmployerProfileForm(forms.ModelForm):

    class Meta:

        def __init__(self):
            pass

        model = CustomEmployer
        exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name',
                   'is_staff', 'is_active', 'date_joined',)


class AgencyProfileForm(forms.ModelForm):

    class Meta:

        def __init__(self):
            pass

        model = CustomAgency
        exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name',
                   'is_staff', 'is_active', 'date_joined',)
