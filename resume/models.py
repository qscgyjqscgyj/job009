# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from main.models import *


class Resume(models.Model):
    owner = models.ForeignKey(User, verbose_name=_(u'Владелец резюме'), blank=True, null=True)
    date = models.DateTimeField(verbose_name=_(u'Дата добавления'), auto_now=True)
    office = models.CharField(verbose_name=_(u'Должность'), max_length=50)
    category = models.ForeignKey(AdCategory, verbose_name=_(u'Рубрика'), related_name='resume_category')
    subcategory = models.ManyToManyField(AdSubCategory, verbose_name=_(u'Подрубрика'), related_name='resume_subcategory')
    schedule = models.ForeignKey(AdSchedule, verbose_name=_(u'График работы'), related_name='resume_schedule',
                                 blank=True, null=True)
    employment = models.ForeignKey(AdEmployment, verbose_name=_(u'Тип занятости'), related_name='resume_employment',
                                   blank=True, null=True)
    salary = models.CharField(verbose_name=_(u'Зарплата'), max_length=50, blank=True, null=True)
    salary_measure = models.ForeignKey(AdSalaryMeasure, verbose_name=_(u'Валюта'),
                                       related_name='resume_salary_measure', blank=True, null=True)
    fio = models.CharField(verbose_name=_(u'Ф.И.О.'), max_length=50)
    photo = models.ImageField(verbose_name=_(u'Фото'), upload_to='resume_photo', blank=True, null=True)
    birth = models.DateField(verbose_name=_(u'Полных лет'))
    gender = models.ForeignKey(Gender, verbose_name=_(u'Пол'), related_name='resume_gender')
    marital_status = models.ForeignKey(MaritalStatus, verbose_name=_(u'Семейное положение'),
                                       related_name='resume_marital_status', blank=True, null=True)
    experience = models.ForeignKey(AdExperience, verbose_name=_(u'Общий стаж работы'), related_name='resume_experience',
                                   blank=True, null=True)
    skills = models.TextField(verbose_name=_(u'Опыт работы и профессиональные навыки'))
    education = models.ForeignKey(Education, verbose_name=_(u'Образование'), related_name='resume_education')
    institution = models.CharField(verbose_name=_(u'Учебное заведение'), max_length=50, blank=True, null=True)
    diploma = models.CharField(verbose_name=_(u'Основная специальность по диплому'), max_length=50,
                               blank=True, null=True)
    ex_education = models.TextField(verbose_name=_(u'Доп. образование'), blank=True, null=True)
    qualities = models.TextField(verbose_name=_(u'Личные качества'), blank=True, null=True)
    driving_license = models.BooleanField(verbose_name=_(u'Водительские права'))
    business_trip = models.BooleanField(verbose_name=_(u'Готовность к командировкам'))
    file_resume = models.FileField(verbose_name=_(u'Резюме'), upload_to='resume_file', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name=_(u'Город проживания'), related_name='resume_city')
    area = models.ForeignKey(AdArea, verbose_name=_(u'Район проживания'), related_name='resume_area',
                             blank=True, null=True)
    phone = models.CharField(verbose_name=_(u'Телефон'), max_length=100, blank=True, null=True)
    phone_details = models.CharField(verbose_name=_(u'Дополнительная информация'), max_length=100,
                                     blank=True, null=True)
    email = models.EmailField(verbose_name=_(u'E-mail'))
    icq = models.CharField(verbose_name=_(u'ICQ'), max_length=20, blank=True, null=True)
    skype = models.CharField(verbose_name=_(u'Skype'), max_length=50, blank=True, null=True)
    work_area = models.ManyToManyField(AdArea, verbose_name=_(u'Желаемые районы для работы'),
                                       related_name='resume_work_area', blank=True, null=True)
    move = models.BooleanField(verbose_name=_(u'Переезд'))
    ad_time = models.ForeignKey(AdTime, verbose_name=_(u'Время жизни резюме'), related_name='resume_ad_time',
                                blank=True, null=True)
    captcha = CaptchaField()
    rating = models.IntegerField(verbose_name=_(u'Рейтинг объявления'), blank=True, null=True)

    def __unicode__(self):
        return self.office

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Резюме')
        verbose_name_plural = _(u'Резюме')