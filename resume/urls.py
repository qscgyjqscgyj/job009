# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from registration.backends.default.views import ActivationView
from resume.views import ResumeFormView
from user_profile.views import ApplicantRegistrationView, my_change_password, EmployerRegistrationView, AgencyRegistrationView, CustomProfileView

urlpatterns = patterns(
    '',
    url(r'^add/$',
       ResumeFormView.as_view(template_name='resume.html'), name='add_resume'),
)