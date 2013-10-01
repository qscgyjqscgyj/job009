# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from registration.forms import RegistrationForm
from django import forms


class CustomRegistrationForm(RegistrationForm):
    captcha = CaptchaField()


#class FirmProfileForm(forms.ModelForm):
#
#    class Meta:
#        model = CustomFirm
#        exclude = ('password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name',
#                   'is_staff', 'is_active', 'date_joined',)
