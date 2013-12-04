# -*- coding: utf-8 -*-
from django.contrib import admin
from resume.models import *
from flatblocks.forms import FlatBlockForm
from flatblocks.models import FlatBlock
from redactor.widgets import RedactorEditor


class AdCategoryInline(admin.TabularInline):
    model = AdSubCategory
    fk_name = "category"


class AdCategoryAdmin(admin.ModelAdmin):
    inlines = [
        AdCategoryInline,
    ]
    ordering = ['name']


class AdSubCategotyAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'category', )

admin.site.register(AdCategory, AdCategoryAdmin)
admin.site.register(AdSubCategory, AdSubCategotyAdmin)
admin.site.register(AdSchedule)
admin.site.register(AdSalaryMeasure)
admin.site.register(AdEmployment)
admin.site.register(AdExperience)
admin.site.register(AdArea)
#admin.site.register(AdTime)
admin.site.register(Gender)
admin.site.register(MaritalStatus)
admin.site.register(Education)
#admin.site.register(Position)
#admin.site.register(Employees)
#admin.site.register(CompanyCategory)
admin.site.register(City)
admin.site.register(TopBanner)
admin.site.register(MiddleBanner)
admin.site.register(RightBanner)


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






