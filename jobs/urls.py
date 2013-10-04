# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from jobs.views import JobFormView

urlpatterns = patterns(
    '',
    url(r'^add/$',
       JobFormView.as_view(template_name='job.html'), name='add_job'),
)