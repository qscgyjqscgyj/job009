# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from main.views import MainJobsView, MainResumeView


urlpatterns = patterns('',
    url(r'^$', MainJobsView.as_view(), name='main_jobs'),
    url(r'^resume/$', MainResumeView.as_view(), name='main_resume'),
)
