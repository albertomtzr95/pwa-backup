from django.contrib import admin

from apps.companies.models import *


class CompanyAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['folio', 'name', 'contact_name', 'contact_phone']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['folio', 'name', 'country', 'contact_name', 'is_active', 'is_deleted', 'cutoff_date', 'created_at',
                    'updated_at']


admin.site.register(Company, CompanyAdmin)
