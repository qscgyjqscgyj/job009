# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_geoip.models import GeoLocationFacade, City
from registration.models import RegistrationManager


class CustomLocation(GeoLocationFacade):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='custom_location')

    def __init__(self):
        pass

    def __unicode__(self):
        return self.name

    @classmethod
    def get_available_locations(cls):
        return City.objects.all()


class Gender(models.Model):
    name = models.CharField(verbose_name=_(u'Пол'), max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Пол')
        verbose_name_plural = _(u'Пол')


class MaritalStatus(models.Model):
    name = models.CharField(verbose_name=_(u'Семейное положение'), max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Семейное положение')
        verbose_name_plural = _(u'Семейное положение')


class Education(models.Model):
    name = models.CharField(verbose_name=_(u'Образование'), max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Образование')
        verbose_name_plural = _(u'Образование')


#соискатель
class CustomApplicant(User):
    fio = models.CharField(verbose_name=_(u'Ф.И.О.'), max_length=100)
    photo = models.ImageField(verbose_name=_(u'Фото'), upload_to='applicant_photo')
    birth = models.DateField(verbose_name=_(u'Дата рождения'), blank=True, null=True)
    gender = models.ForeignKey(Gender, verbose_name=_(u'Пол'), related_name='applicant_gender', blank=True, null=True)
    marital_status = models.ForeignKey(MaritalStatus, verbose_name=_(u'Семейное положение'),
                                       related_name='applicant_marital_status', blank=True, null=True)
    education = models.ForeignKey(Education, verbose_name=_(u'Образование'), related_name='applicant_education', blank=True, null=True)
    professional_goals = models.TextField(verbose_name=_(u'Профессиональные цели'), blank=True, null=True)
    interests = models.TextField(verbose_name=_(u'Интересы'), blank=True, null=True)
    city = models.ForeignKey(City, verbose_name=_(u'Город'), blank=True, null=True)
    phone = models.CharField(verbose_name=_(u'Телефон'), max_length=100, blank=True, null=True)
    phone_details = models.CharField(verbose_name=_(u'Дополнительная информация'), max_length=100, blank=True, null=True)
    icq = models.CharField(verbose_name=_(u'ICQ'), max_length=20, blank=True, null=True)
    skype = models.CharField(verbose_name=_(u'Skype'), max_length=50, blank=True, null=True)
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
