# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_geoip.models import GeoLocationFacade
from registration.models import RegistrationManager
from main.models import Gender, MaritalStatus, Education, Position, CompanyCategory, Employees, City


class CustomLocation(GeoLocationFacade):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='custom_location_city')

    def __init__(self):
        pass

    def __unicode__(self):
        return unicode(self.name)

    @classmethod
    def get_available_locations(cls):
        return City.objects.all().order_by('name')


#соискатель
class CustomApplicant(User):
    fio = models.CharField(verbose_name=_(u'Ф.И.О.'), max_length=100)
    photo = models.ImageField(verbose_name=_(u'Фото'), upload_to='applicant_photo')
    birth = models.CharField(verbose_name=_(u'Полных лет'), max_length=100, blank=True, null=True)
    gender = models.ForeignKey(Gender, verbose_name=_(u'Пол'), related_name='applicant_gender', blank=True, null=True)
    marital_status = models.ForeignKey(MaritalStatus, verbose_name=_(u'Семейное положение'),
                                       related_name='applicant_marital_status', blank=True, null=True)
    education = models.ForeignKey(Education, verbose_name=_(u'Образование'), related_name='applicant_education',
                                  blank=True, null=True)
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
        return unicode(self.username)

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Соискатель')
        verbose_name_plural = _(u'Соискатели')


#работодатель
class CustomEmployer(User):
    contact = models.CharField(verbose_name=_(u'Контактное лицо'), max_length=100, blank=True, null=True)
    position = models.ForeignKey(Position, verbose_name=_(u'Должность в компании'),
                                 related_name='employer_position', blank=True, null=True)
    phone = models.CharField(verbose_name=_(u'Телефон'), max_length=20, blank=True, null=True)
    company_name = models.CharField(verbose_name=_(u'Название компании'), max_length=100, blank=True, null=True)
    legal_company_name = models.CharField(verbose_name=_(u'Юридическое название компании'),
                                          max_length=100, blank=True, null=True)
    photo = models.ImageField(verbose_name=_(u'Логотип'), upload_to='employer_photo', blank=True, null=True)
    site = models.URLField(verbose_name=_(u'Адрес сайта'), max_length=100, blank=True, null=True)
    company_categories = models.ManyToManyField(CompanyCategory, verbose_name=_(u'Рубрики'),
                                                related_name='employer_company_categories', blank=True, null=True)
    employees = models.ForeignKey(Employees, verbose_name=_(u'Количество сотрудников'),
                                  related_name='employer_number_of_employees', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name=_(u'Город'), blank=True, null=True)
    street = models.CharField(verbose_name=_(u'Улица'), max_length=100, blank=True, null=True)
    building = models.CharField(verbose_name=_(u'Здание'), max_length=20, blank=True, null=True)
    about_address = models.CharField(verbose_name=_(u'Дополнительная информация о адресе'), max_length=100, blank=True,
                                     null=True)
    captcha = CaptchaField()

    objects = RegistrationManager()

    def __unicode__(self):
        return unicode(self.username)

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Работодатель')
        verbose_name_plural = _(u'Работодатели')


#кадровое агентство
class CustomAgency(User):
    contact = models.CharField(verbose_name=_(u'Контактное лицо'), max_length=100, blank=True, null=True)
    position = models.ForeignKey(Position, verbose_name=_(u'Должность в компании'),
                                 related_name='agency_position', blank=True, null=True)
    phone = models.CharField(verbose_name=_(u'Телефон'), max_length=20, blank=True, null=True)
    company_name = models.CharField(verbose_name=_(u'Название компании'), max_length=100, blank=True, null=True)
    legal_company_name = models.CharField(verbose_name=_(u'Юридическое название компании'),
                                          max_length=100, blank=True, null=True)
    photo = models.ImageField(verbose_name=_(u'Логотип'), upload_to='agency_photo', blank=True, null=True)
    site = models.URLField(verbose_name=_(u'Адрес сайта'), max_length=100, blank=True, null=True)
    company_categories = models.ManyToManyField(CompanyCategory, verbose_name=_(u'Рубрики'),
                                                related_name='agency_company_categories', blank=True, null=True)
    employees = models.ForeignKey(Employees, verbose_name=_(u'Количество сотрудников'),
                                  related_name='agency_number_of_employees', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name=_(u'Город'), blank=True, null=True)
    street = models.CharField(verbose_name=_(u'Улица'), max_length=100, blank=True, null=True)
    building = models.CharField(verbose_name=_(u'Здание'), max_length=20, blank=True, null=True)
    about_address = models.CharField(verbose_name=_(u'Дополнительная информация о адресе'), max_length=100, blank=True,
                                     null=True)
    captcha = CaptchaField()

    objects = RegistrationManager()

    def __unicode__(self):
        return unicode(self.username)

    class Meta:

        def __init__(self):
            pass

        verbose_name = _(u'Кадровое агентство')
        verbose_name_plural = _(u'Кадровые агентства')
