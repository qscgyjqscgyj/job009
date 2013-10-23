# -*- coding: utf-8 -*-
from django.contrib import admin
from resume.models import *
from flatblocks.forms import FlatBlockForm
from flatblocks.models import FlatBlock
from redactor.widgets import RedactorEditor


admin.site.register(AdCategory)
admin.site.register(AdSubCategory)
admin.site.register(AdSchedule)
admin.site.register(AdSalaryMeasure)
admin.site.register(AdEmployment)
admin.site.register(AdExperience)
admin.site.register(AdArea)
admin.site.register(AdTime)
admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(Education)
admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(CompanyCategory)


class CustomFlatBlockForm(FlatBlockForm):
    class Meta:

        def __init__(self):
            pass

        widgets = {
            'content': RedactorEditor(),
        }


class CustomFlatBlockAdmin(admin.ModelAdmin):
    form = CustomFlatBlockForm


admin.site.unregister(FlatBlock)
admin.site.register(FlatBlock, CustomFlatBlockAdmin)






