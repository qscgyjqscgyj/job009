# -*- coding: utf-8 -*-
from dajaxice.core import dajaxice_config
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^geoip/', include('django_geoip.urls')),
    url(r'^accounts/', include('user_profile.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^flatblocks/', include("flatblocks.urls")),
    url(r'^resume/', include('resume.urls')),
    url(r'^job/', include('jobs.urls')),
    url(r'^', include('main.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
