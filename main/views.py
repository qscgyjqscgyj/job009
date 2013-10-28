# -*- coding: utf-8 -*-
from django.views.generic import ListView
from jobs.models import Job
from resume.models import Resume
import urllib
from bs4 import BeautifulSoup


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
    soup = BeautifulSoup(page.read(), from_encoding="utf-8")
    weather = soup.find(id='weather-banner')
    weather_td = weather.findAll('td')
    currency = soup.find(id='currency-banner')
    currency_td = currency.findAll('td')
    banners = {'weather_date': weather.th.text, 'weather_night': weather_td[1].text.encode('utf-8'),
               'weather_day': weather_td[3].text.encode('utf-8'), 'currency_date': currency.th.text,
               'currency_usd': currency_td[1].text, 'currency_eur': currency_td[3].text}
    return {'banners': banners}
