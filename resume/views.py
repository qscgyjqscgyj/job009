# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django_geoip.models import City, Region
from main.models import MaritalStatus, AdSubCategory, Gender
from resume.forms import ResumeForm, ResumeAuthForm
from user_profile.models import CustomEmployer


class ResumeFormView(FormView):
    template_name = 'resume.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ResumeFormView, self).get_context_data(**kwargs)
        user = self.request.user
        try:
            employer = CustomEmployer.objects.get(pk=user.pk).pk
        except ObjectDoesNotExist:
            employer = False
        if user.pk == employer:
            context['employer'] = True
        return context

    def get_form_class(self):
        self.form_class = ResumeForm
        if self.request.user.is_authenticated():
            self.form_class = ResumeAuthForm
        return self.form_class

    def get_form_kwargs(self):
        kwargs = super(ResumeFormView, self).get_form_kwargs()
        #self.form_class.base_fields['marital_status'].queryset = MaritalStatus.objects.none()
        return kwargs

    def form_valid(self, form_class):
        if self.request.method == 'POST':
            if form_class.is_valid():
                try:
                    message = form_class.save()
                    message.owner = self.request.user.customapplicant
                    message.save()
                    return HttpResponseRedirect(self.get_success_url())
                except ObjectDoesNotExist and AttributeError:
                    try:
                        message = form_class.save()
                        message.owner = self.request.user.customemployer
                        message.save()
                        return HttpResponseRedirect(self.get_success_url())
                    except ObjectDoesNotExist and AttributeError:
                        try:
                            message = form_class.save()
                            message.owner = self.request.user.customagency
                            message.save()
                            return HttpResponseRedirect(self.get_success_url())
                        except ObjectDoesNotExist and AttributeError:
                            message = form_class.save()
                            message.save()
                            return HttpResponseRedirect(self.get_success_url())