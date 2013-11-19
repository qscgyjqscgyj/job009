# -*- coding: utf-8 -*-
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django_geoip.models import City
from jobs.forms import JobForm
from user_profile.models import CustomApplicant


class JobFormView(FormView):
    form_class = JobForm
    template_name = 'job.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(JobFormView, self).get_context_data(**kwargs)
        user = self.request.user
        try:
            applicant = CustomApplicant.objects.get(pk=user.pk).pk
        except ObjectDoesNotExist:
            applicant = False
        if user.pk == applicant:
            context['applicant'] = True
        return context

    def get_form_kwargs(self):
        kwargs = super(JobFormView, self).get_form_kwargs()
        #self.form_class.base_fields['city'].queryset = City.objects.all().order_by('name')
        return kwargs

    def form_valid(self, form_class):
        if self.request.method == 'POST':
            if form_class.is_valid():
                try:
                    message = form_class.save()
                    message.owner = self.request.user.customapplicant
                    message.save()
                    return HttpResponseRedirect(self.get_success_url())
                except ObjectDoesNotExist:
                    try:
                        message = form_class.save()
                        message.owner = self.request.user.customemployer
                        message.save()
                        return HttpResponseRedirect(self.get_success_url())
                    except ObjectDoesNotExist:
                        message = form_class.save()
                        message.owner = self.request.user.customagency
                        message.save()
                        return HttpResponseRedirect(self.get_success_url())