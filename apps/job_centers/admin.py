from django.contrib import admin

from apps.job_centers.models import *


class JobCenterAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name', 'business_name', 'health_manager', 'company']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'business_name', 'health_manager', 'company', 'is_active', 'is_deleted', 'created_at',
                    'updated_at']


admin.site.register(JobCenter, JobCenterAdmin)
