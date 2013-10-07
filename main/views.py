# -*- coding: utf-8 -*-
from django.views.generic import ListView
from jobs.models import Job
from resume.models import Resume


class MainView(ListView):
    model = Job
    template_name = 'base.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['resume'] = Resume.objects.all()
        context['jobs'] = Job.objects.all()
        return context
