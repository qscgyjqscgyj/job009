# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from resume.views import ResumeFormView, ResumeDetailView, UserResumeView, DeleteUserResume, ChangeUserResume

urlpatterns = patterns('',
    url(r'^add/$', ResumeFormView.as_view(template_name='resume.html'), name='add_resume'),
    url(r'^(?P<pk>\d+)/$', ResumeDetailView.as_view(), name='resume_detail'),
    url(r'^my/$', UserResumeView.as_view(), name='user_resume'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteUserResume.as_view(), name='delete_user_resume'),
    url(r'^change/(?P<pk>\d+)/$', ChangeUserResume.as_view(), name='change_user_resume'),
)