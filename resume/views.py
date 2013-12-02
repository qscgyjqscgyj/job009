# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.views.generic import FormView, DetailView, ListView, DeleteView, UpdateView
from resume.forms import ResumeForm, ResumeAuthForm
from resume.models import Resume
from user_profile.models import CustomEmployer, CustomApplicant


class ResumeFormView(FormView):
    template_name = 'resume.html'
    success_url = '/accounts/profile'

    def get_success_url(self):
        try:
            if self.request.user.customapplicant:
                url = '/resume/my'
                return url
        except ObjectDoesNotExist and AttributeError:
            url = '/resume'
            return url

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
        try:
            self.form_class.base_fields['fio'].initial = self.request.user.customapplicant.fio
            self.form_class.base_fields['email'].initial = self.request.user.customapplicant.email
            self.form_class.base_fields['photo'].initial = self.request.user.customapplicant.photo
            self.form_class.base_fields['birth'].initial = self.request.user.customapplicant.birth
            self.form_class.base_fields['gender'].initial = self.request.user.customapplicant.gender
            self.form_class.base_fields['marital_status'].initial = self.request.user.customapplicant.marital_status
            self.form_class.base_fields['education'].initial = self.request.user.customapplicant.education
            self.form_class.base_fields['city'].initial = self.request.user.customapplicant.city
            self.form_class.base_fields['phone'].initial = self.request.user.customapplicant.phone
            self.form_class.base_fields['phone_details'].initial = self.request.user.customapplicant.phone_details
            self.form_class.base_fields['education'].initial = self.request.user.customapplicant.education
            self.form_class.base_fields['institution'].initial = self.request.user.customapplicant.institution
            self.form_class.base_fields['ex_education'].initial = self.request.user.customapplicant.ex_education
            self.form_class.base_fields['diploma'].initial = self.request.user.customapplicant.diploma
            return kwargs
        except ObjectDoesNotExist and AttributeError:
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


class ResumeDetailView(DetailView):
    model = Resume
    pk_url_kwarg = 'pk'
    context_object_name = 'resume'
    template_name = 'resume-detail.html'


class UserResumeView(ListView):
    model = Resume
    template_name = 'user-resume.html'

    def get_context_data(self, **kwargs):
        context = super(UserResumeView, self).get_context_data(**kwargs)
        try:
            user = CustomApplicant.objects.get(username=self.request.user.customapplicant.username)
            context['resume'] = Resume.objects.filter(owner=user)
            return context
        except ObjectDoesNotExist and AttributeError:
            return context


class DeleteUserResume(DeleteView):
    model = Resume
    template_name = 'delete-user-resume.html'
    success_url = '/resume/my'

    def delete(self, request, *args, **kwargs):
        if request.user == Resume.objects.get(pk=kwargs['pk']).owner:
            return super(DeleteUserResume, self).delete(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/resume/my')


class ChangeUserResume(UpdateView):
    model = Resume
    success_url = '/resume/my'
    template_name = 'change-user-resume.html'
    form_class = ResumeAuthForm