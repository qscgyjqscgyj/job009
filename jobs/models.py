# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from main.models import *


class Job(models.Model):
    owner = models.ForeignKey(User, verbose_name=_(u'Владелец вакансии'), blank=True, null=True)
    date = models.DateTimeField(verbose_name=_(u'Дата добавления'), auto_now=True)
    office = models.CharField(verbose_name=_(u'Должность'), max_length=50)
    category = models.ForeignKey(AdCategory, verbose_name=_(u'Рубрика'), related_name='job_category')
    schedule = models.ForeignKey(AdSchedule, verbose_name=_(u'График работы'), related_name='job_schedule',
                                 blank=True, null=True)
    employment = models.ForeignKey(AdEmployment, verbose_name=_(u'Тип занятости'), related_name='job_employment',
                                   blank=True, null=True)
    salary_from = models.CharField(verbose_name=_(u'Зарплата (от)'), max_length=50, blank=True, null=True)
    salary_to = models.CharField(verbose_name=_(u'Зарплата (до)'), max_length=50, blank=True, null=True)
    salary_measure = models.ForeignKey(AdSalaryMeasure, verbose_name=_(u'Валюта'),
                                       related_name='job_salary_measure', blank=True, null=True)
    about_job = models.TextField(verbose_name=_(u'Подробное описание вакансии'))
    city = models.ForeignKey(City, verbose_name=_(u'Город проживания'), related_name='job_city')
    another_city_candidate = models.NullBooleanField(verbose_name=_(u'Рассматриваются ли кандидаты из других городов'),
                                                     blank=True, null=True)
    street = models.CharField(verbose_name=_(u'Улица'), max_length=50, blank=True, null=True)
    building = models.CharField(verbose_name=_(u'Здание'), max_length=50, blank=True, null=True)
    about_address = models.CharField(verbose_name=_(u'Дополнительная информация'), max_length=50, blank=True, null=True)
    education = models.ForeignKey(Education, verbose_name=_(u'Образование'), related_name='job_education',
                                  blank=True, null=True)
    experience = models.ForeignKey(AdExperience, verbose_name=_(u'Стаж работы'), related_name='job_experience',
                                   blank=True, null=True)
    skills = models.TextField(verbose_name=_(u'Опыт работы и профессиональные навыки'))
    driving_license = models.NullBooleanField(verbose_name=_(u'Водительские права'), blank=True, null=True)
    business_trip = models.NullBooleanField(verbose_name=_(u'Возможные командировки'), blank=True, null=True)
    smoke = models.NullBooleanField(verbose_name=_(u'Курит ли'), blank=True, null=True)
    area = models.ForeignKey(AdArea, verbose_name=_(u'Район места работы'), related_name='job_area',
                             blank=True, null=True)
    phone = models.CharField(verbose_name=_(u'Телефон'), max_length=100)
    phone_details = models.CharField(verbose_name=_(u'Дополнительная информация'), max_length=100,
                                     blank=True, null=True)
    email = models.EmailField(verbose_name=_(u'E-mail'))
    icq = models.CharField(verbose_name=_(u'ICQ'), max_length=20, blank=True, null=True)
    skype = models.CharField(verbose_name=_(u'Skype'), max_length=50, blank=True, null=True)
    move = models.NullBooleanField(verbose_name=_(u'Переезд'), blank=True, null=True)
    move_cities = models.ManyToManyField(City, verbose_name=_(u'Возможные города для переезда'), blank=True, null=True)
    ad_time = models.ForeignKey(AdTime, verbose_name=_(u'Время жизни вакансии'), related_name='job_ad_time',
                                blank=True, null=True)
    captcha = CaptchaField()
    rating = models.IntegerField(verbose_name=_(u'Рейтинг объявления'), blank=True, null=True)

    def __unicode__(self):
        return self.office

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Вакансия')
        verbose_name_plural = _(u'Вакансии')