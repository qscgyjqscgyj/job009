# -*- coding: utf-8 -*-
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, DetailView, DeleteView, UpdateView
from django_geoip.models import City
from jobs.forms import JobForm
from jobs.models import Job
from user_profile.models import CustomApplicant, CustomEmployer


class JobFormView(FormView):
    form_class = JobForm
    template_name = 'job.html'
    success_url = '/job/my'

    def get_context_data(self, **kwargs):
        context = super(JobFormView, self).get_context_data(**kwargs)
        user = self.request.user
        try:
            applicant = CustomApplicant.objects.get(pk=user.pk).pk
            if user.pk == applicant:
                context['applicant'] = True
        except ObjectDoesNotExist:
            try:
                context['employer'] = self.request.user.customemployer
            except ObjectDoesNotExist and AttributeError:
                return context
        return context

    def get_form_kwargs(self):
        kwargs = super(JobFormView, self).get_form_kwargs()
        try:
            self.form_class.base_fields['email'].initial = self.request.user.customemployer.email
            self.form_class.base_fields['city'].initial = self.request.user.customemployer.city
            self.form_class.base_fields['phone'].initial = self.request.user.customemployer.phone
            self.form_class.base_fields['phone_details'].initial = self.request.user.customemployer.phone_details
            self.form_class.base_fields['street'].initial = self.request.user.customemployer.street
            self.form_class.base_fields['building'].initial = self.request.user.customemployer.building
            self.form_class.base_fields['about_address'].initial = self.request.user.customemployer.about_address
            return kwargs
        except ObjectDoesNotExist:
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


class JobDetailView(DetailView):
    model = Job
    pk_url_kwarg = 'pk'
    context_object_name = 'job'
    template_name = 'job-detail.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetailView, self).get_context_data(**kwargs)
        try:
            if self.request.user.pk == CustomApplicant.objects.get(pk=self.request.user.pk).pk:
                context['applicant'] = True
                return context
        except ObjectDoesNotExist:
            try:
                if self.request.user.pk == CustomEmployer.objects.get(pk=self.request.user.pk).pk:
                    context['employer'] = True
                    return context
            except ObjectDoesNotExist:
                return context



class UserJobsView(ListView):
    model = Job
    template_name = 'user-jobs.html'

    def get_context_data(self, **kwargs):
        context = super(UserJobsView, self).get_context_data(**kwargs)
        try:
            user = CustomEmployer.objects.get(username=self.request.user.customemployer.username)
            context['jobs'] = Job.objects.filter(owner=user)
            return context
        except ObjectDoesNotExist and AttributeError:
            return context


class DeleteUserJob(DeleteView):
    model = Job
    template_name = 'delete-user-job.html'
    success_url = '/job/my'

    def delete(self, request, *args, **kwargs):
        if request.user == Job.objects.get(pk=kwargs['pk']).owner:
            return super(DeleteUserJob, self).delete(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/job/my')


class ChangeUserJob(UpdateView):
    model = Job
    success_url = '/job/my'
    template_name = 'change-user-job.html'
    form_class = JobForm