# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from jobs.views import JobFormView, UserJobsView, JobDetailView, DeleteUserJob, ChangeUserJob

urlpatterns = patterns('',
    url(r'^add/$',
        login_required(JobFormView.as_view(template_name='job.html')), name='add_job'),
        url(r'^my/$', UserJobsView.as_view(), name='user_jobs'),
        url(r'^(?P<pk>\d+)/$', JobDetailView.as_view(), name='job_detail'),
        url(r'^delete/(?P<pk>\d+)/$', DeleteUserJob.as_view(), name='delete_user_job'),
        url(r'^change/(?P<pk>\d+)/$', ChangeUserJob.as_view(), name='change_user_resume'),

    )