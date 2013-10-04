# -*- coding: utf-8 -*-
from django.views.generic import FormView
from django_geoip.models import City
from jobs.forms import JobForm


class JobFormView(FormView):
    form_class = JobForm
    template_name = 'job.html'

    def get_form_kwargs(self):
        kwargs = super(JobFormView, self).get_form_kwargs()
        self.form_class.base_fields['city'].queryset = City.objects.all().order_by('name')
        return kwargs