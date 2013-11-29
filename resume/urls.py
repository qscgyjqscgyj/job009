# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from resume.views import ResumeFormView, ResumeDetailView, UserResumeView, DeleteUserResume, ChangeUserResume
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^add/$', ResumeFormView.as_view(template_name='resume.html'), name='add_resume'),
    url(r'^(?P<pk>\d+)/$', ResumeDetailView.as_view(), name='resume_detail'),
    url(r'^my/$', login_required(UserResumeView.as_view(), login_url='/accounts/login/'), name='user_resume'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteUserResume.as_view(), login_url='/accounts/login/'),
        name='delete_user_resume'),
    url(r'^change/(?P<pk>\d+)/$', login_required(ChangeUserResume.as_view(), login_url='/accounts/login/'),
        name='change_user_resume'),
)