# -*- coding: utf-8 -*-
from django.views.generic import ListView
from jobs.models import Job
from resume.models import Resume
import urllib
import lxml.html


class MainView(ListView):
    model = Job
    template_name = 'base.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['resume'] = Resume.objects.all()
        context['jobs'] = Job.objects.all()
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
