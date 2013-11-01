# -*- coding: utf-8 -*-
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from jobs.models import Job
from resume.models import Resume
import urllib
import lxml.html


class MainJobsView(ListView):
    model = Job
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(MainJobsView, self).get_context_data(**kwargs)
        job_list = Job.objects.all()
        if self.request.GET.get('show'):
            show_get = self.request.GET.get('show')
            try:
                int(show_get)
                if int(show_get) != 10 and int(show_get) != 30 and int(show_get) != 50:
                    show = 10
                else:
                    show = int(show_get)
            except ValueError:
                show = 10
        else:
            show = 10
        job_paginator = Paginator(job_list, show)
        page = self.request.GET.get('page')
        try:
            jobs = job_paginator.page(page)
        except PageNotAnInteger:
            jobs = job_paginator.page(1)
        except EmptyPage:
            jobs = job_paginator.page(job_paginator.num_pages)
        context['jobs'] = jobs
        context['jobs_len'] = len(Job.objects.all())
        context['jobs_all_pages'] = job_paginator.count
        context['show'] = show
        return context


class MainResumeView(ListView):
    model = Resume
    template_name = 'resume-list.html'

    def get_context_data(self, **kwargs):
        context = super(MainResumeView, self).get_context_data(**kwargs)
        resume_list = Resume.objects.all()
        if self.request.GET.get('show'):
            show_get = self.request.GET.get('show')
            try:
                int(show_get)
                if int(show_get) != 10 and int(show_get) != 30 and int(show_get) != 50:
                    show = 10
                else:
                    show = int(show_get)
            except ValueError:
                show = 10
        else:
            show = 10
        resume_paginator = Paginator(resume_list, show)
        page = self.request.GET.get('page')
        try:
            resume = resume_paginator.page(page)
        except PageNotAnInteger:
            resume = resume_paginator.page(1)
        except EmptyPage:
            resume = resume_paginator.page(resume_paginator.num_pages)
        context['resume'] = resume
        context['resume_len'] = len(Resume.objects.all())
        context['resume_all_pages'] = resume_paginator.count
        context['show'] = show
        return context


def get_banners_info(page):
    page = urllib.urlopen("http://www.2-999-999.ru/")
    soup = lxml.html.document_fromstring(page.read())
    weather = soup.get_element_by_id(id='weather-banner')
    currency = soup.get_element_by_id(id='currency-banner')
    weather_date = weather.find('table').findall('tr')[0].find('th').text
    weather_night = weather.find('table').findall('tr')[1].findall('td')[1].text
    weather_day = weather.find('table').findall('tr')[2].findall('td')[1].text
    currency_date = currency.find('table').findall('tr')[0].find('th').text
    currency_usd = currency.find('table').findall('tr')[1].findall('td')[1].text
    currency_eur = currency.find('table').findall('tr')[2].findall('td')[1].text
    banners = {'weather_date': weather_date, 'weather_night': weather_night,
               'weather_day': weather_day, 'currency_date': currency_date,
               'currency_usd': currency_usd, 'currency_eur': currency_eur}
    return {'banners': banners}
