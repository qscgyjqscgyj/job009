# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from jobs.views import JobFormView

urlpatterns = patterns(
    '',
    url(r'^add/$',
        login_required(JobFormView.as_view(template_name='job.html')), name='add_job'),
    )