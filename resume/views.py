# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django_geoip.models import City, Region
from main.models import MaritalStatus, AdSubCategory
from resume.forms import ResumeForm


class ResumeFormView(FormView):
    form_class = ResumeForm
    template_name = 'resume.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(ResumeFormView, self).get_form_kwargs()
        #self.form_class.base_fields['city'].queryset = City.objects.filter(region=Region.objects.get(pk=80))
        self.form_class.base_fields['marital_status'].queryset = MaritalStatus.objects.filter(pk=1)
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

    #def post(self, *args, **kwargs):
    #    super(ResumeFormView, self).post(self, *args, **kwargs)
    #    if self.request.method == 'POST':
    #        form_class = self.get_form_class()
    #        form = self.get_form(form_class)
    #        form.base_fields['subcategory'].choices = AdSubCategory.objects.all()
    #    if form.is_valid():
    #        return self.form_valid(form)
    #    else:
    #        return self.form_invalid(form)