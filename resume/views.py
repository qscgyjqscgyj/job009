# -*- coding: utf-8 -*-
from django.views.generic import FormView
from django_geoip.models import City
from resume.forms import ResumeForm


class ResumeFormView(FormView):
    form_class = ResumeForm
    template_name = 'resume.html'

    def get_form_kwargs(self):
        kwargs = super(ResumeFormView, self).get_form_kwargs()
        self.form_class.base_fields['city'].queryset = City.objects.all().order_by('name')
        return kwargs