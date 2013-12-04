# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from main.mixins import SlugTraits


class City(models.Model):
    name = models.CharField(verbose_name=_(u'Город'), max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Город')
        verbose_name_plural = _(u'Города')


class AdCategory(SlugTraits(), models.Model):
    name = models.CharField(verbose_name=_(u'Название рубрики'), max_length=50)
    #subcategory = models.ManyToManyField(AdSubCategory, verbose_name=_(u'Подрубкрика'),
    #                                     related_name='ad_category_subcategory')

    @models.permalink
    def get_absolute_url(self):
        return ('main.base', (), {'slug': self.slug})

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Рубрика')
        verbose_name_plural = _(u'Рубрики')


class AdSubCategory(models.Model):
    name = models.CharField(verbose_name=_(u'Название подрубрики'), max_length=50)
    category = models.ForeignKey(AdCategory, verbose_name=_(u'Рубрика'), related_name='ad_sub_category_category')

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Подрубрика')
        verbose_name_plural = _(u'Подрубрики')


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
    city = models.ForeignKey(City, verbose_name=_(u'Город'), related_name='areas')
    name = models.CharField(verbose_name=_(u'Район проживания'), max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Район')
        verbose_name_plural = _(u'Районы')


class AdTime(models.Model):
    name = models.CharField(verbose_name=_(u'Время жизни объявления'), max_length=50)
    #time = models.IntegerField(verbose_name=_(u'Число'))

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


class Position(models.Model):
    name = models.CharField(verbose_name=_(u'Позиция'), max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Позиция')
        verbose_name_plural = _(u'Позиции в компании')


class CompanyCategory(models.Model):
    name = models.CharField(verbose_name=_(u'Название категории'), max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Категория')
        verbose_name_plural = _(u'Категории компании')


class Employees(models.Model):
    name = models.CharField(verbose_name=_(u'Количество сотрудников'), max_length=20)

    def __unicode__(self):
        return self.name

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Количество сотрудников')
        verbose_name_plural = _(u'Количество сотрудников')


class TopBanner(models.Model):
    image = models.ImageField(verbose_name=_(u'Баннер'), upload_to='top_banner')
    size = models.CharField(verbose_name=_(u'Размер. Пример: 150x150'), max_length=100, blank=True, null=True)
    link = models.URLField(verbose_name=_(u'Ссылка'), max_length=100, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.image)

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Беннер сверху')
        verbose_name_plural = _(u'Баннер сверху')


class MiddleBanner(models.Model):
    image = models.ImageField(verbose_name=_(u'Баннер'), upload_to='middle_banner')
    size = models.CharField(verbose_name=_(u'Размер. Пример: 150x150'), max_length=100, blank=True, null=True)
    link = models.URLField(verbose_name=_(u'Ссылка'), max_length=100, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.image)

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Беннер по середине')
        verbose_name_plural = _(u'Баннеры по середине')


class RightBanner(models.Model):
    image = models.ImageField(verbose_name=_(u'Баннер'), upload_to='right_banner')
    size = models.CharField(verbose_name=_(u'Размер. Пример: 150x150'), max_length=100, blank=True, null=True)
    link = models.URLField(verbose_name=_(u'Ссылка'), max_length=100, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.image)

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Беннер справа')
        verbose_name_plural = _(u'Баннер справа')
