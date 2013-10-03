from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_profile.models import CustomApplicant, CustomEmployer, CustomAgency, CompanyCategory


#class CustomAdmin(UserAdmin):
#    list_display = ('username', 'email', 'is_staff', 'is_active', )
#    list_filter = ('is_staff', 'is_superuser', 'is_active', )
#
#admin.site.register(CustomApplicant)
#admin.site.register(CustomEmployer)
#admin.site.register(CustomAgency)
#admin.site.register(CompanyCategory)

