# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from registration.models import RegistrationManager


#соискатель
class CustomApplicant(User):
    captcha = CaptchaField()

    objects = RegistrationManager()

    def __unicode__(self):
        return self.username

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Соискатель')
        verbose_name_plural = _(u'Соискатели')


#работодатель
class CustomEmployer(User):
    captcha = CaptchaField()

    objects = RegistrationManager()

    def __unicode__(self):
        return self.username

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Работодатель')
        verbose_name_plural = _(u'Работодатели')


#кадровое агентство
class CustomAgency(User):
    captcha = CaptchaField()

    objects = RegistrationManager()

    def __unicode__(self):
        return self.username

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Кадровое агентство')
        verbose_name_plural = _(u'Кадровые агентствая')
