from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user_profile.models import CustomApplicant


class CustomApplicantAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)

admin.site.register(CustomApplicant)

