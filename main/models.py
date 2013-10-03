# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AdCategory(models.Model):
    name = models.CharField(verbose_name=_(u'Название рубрики'), max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Рубрика')
        verbose_name_plural = _(u'Рубрики')


class AdSchedule(models.Model):
    name = models.CharField(verbose_name=_(u'График работы'), max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'График работы')
        verbose_name_plural = _(u'Графики работы')


class AdEmployment(models.Model):
    name = models.CharField(verbose_name=_(u'Тип занятости'), max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Тип занятости')
        verbose_name_plural = _(u'Типы занятости')


class AdSalaryMeasure(models.Model):
    name = models.CharField(verbose_name=_(u'Валюта (зарплата)'), max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Валюта (зарплата)')
        verbose_name_plural = _(u'Типы валют')


class AdExperience(models.Model):
    name = models.CharField(verbose_name=_(u'Стаж работы'), max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Стаж работы')
        verbose_name_plural = _(u'Виды стажа работы')


class AdArea(models.Model):
    name = models.CharField(verbose_name=_(u'Район проживания'), max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Район проживания')
        verbose_name_plural = _(u'Районы проживания')


class AdTime(models.Model):
    name = models.CharField(verbose_name=_(u'Время жизни объявления'), max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Время жизни объявления')
        verbose_name_plural = _(u'Время жизни объявления')


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
