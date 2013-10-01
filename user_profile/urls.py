# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from registration.backends.default.views import ActivationView
from user_profile.views import ApplicantView, ApplicantRegistrationView, my_change_password

urlpatterns = patterns(
    '',
    url(r'^$', ApplicantView.as_view(), name='applicant'),
    url(r'^activate/complete/$',
       TemplateView.as_view(template_name='registration/activation_complete.html'),
       name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$',
       ActivationView.as_view(),
       name='registration_activate'),
    url(r'^register/applicant/$',
       ApplicantRegistrationView.as_view(),
       name='registration_register_user'),
    #url(r'^register/firm/$',
    #   FirmRegistrationView.as_view(),
    #   name='registration_register_firm'),
    url(r'^register/complete/$',
       TemplateView.as_view(template_name='registration/registration_complete.html'),
       name='registration_complete'),
    url(r'^register/closed/$',
       TemplateView.as_view(template_name='registration/registration_closed.html'),
       name='registration_disallowed'),
    (r'', include('registration.auth_urls')),
    #url(r'^profile/$',
    #   login_required(CustomProfileView.as_view()),
    #   name='profile_update'),
    url(r'^password_change/$',
       my_change_password,
       name='change_pass'),
    url(r'^password_change_done$',
       TemplateView.as_view(template_name='registration/password_change_done.html'),
       name='change_pass_done'),

)