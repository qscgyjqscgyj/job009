# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from resume.views import ResumeFormView, ResumeDetailView

urlpatterns = patterns('',
    url(r'^add/$', ResumeFormView.as_view(template_name='resume.html'), name='add_resume'),
    url(r'^(?P<pk>\d+)$', ResumeDetailView.as_view(), name='resume_detail'),
)