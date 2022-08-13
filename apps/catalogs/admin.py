from django.contrib import admin

from apps.catalogs.models import *


class CountryAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class ApplicationMethodAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'job_center', 'is_active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class BusinessActivityAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class CancellationReasonAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class CleaningAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class ConceptAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'type', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at',
                    'deleted_at']


class CustomDescriptionAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class DiscountAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name', 'percentage']
    list_display = ['id', 'name', 'percentage', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at',
                    'deleted_at']


class ExtraAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name', 'quantity']
    list_display = ['id', 'name', 'quantity', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at',
                    'deleted_at']


class IndicationAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name', 'key']
    list_display = ['id', 'name', 'key', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at',
                    'deleted_at']


class InfestationDegreeAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class JobTitleAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class OriginSourceAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class PaymentMethodAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class PaymentWayAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name', 'credit_days']
    list_display = ['id', 'name', 'credit_days', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at',
                    'deleted_at']


class PlagueCategoryAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class PlagueAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name', 'category']
    list_display = ['id', 'name', 'category', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at',
                    'deleted_at']


class PresentationAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class ServiceTypeAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class PriceListAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'key', 'is_active', 'category', 'job_center', 'is_deleted', 'created_at',
                    'updated_at', 'deleted_at']


class PriceListPlagueAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'price_list', 'plague']
    list_display = ['id', 'price_list', 'plague', 'is_active', 'job_center', 'is_deleted', 'created_at',
                    'updated_at', 'deleted_at']


class RejectionReasonAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'job_center', 'is_active', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class StatusAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name', 'key_string', 'module']
    list_display = ['id', 'name', 'key_string', 'module', 'is_active', 'is_deleted', 'created_at', 'updated_at',
                    'deleted_at']


class TaxAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name', 'value', 'is_main']
    list_display = ['id', 'name', 'value', 'is_main', 'is_active', 'is_deleted', 'created_at', 'updated_at',
                    'deleted_at']


class TypeProductAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class UnitProductAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


class VoucherAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['id', 'name']
    list_display = ['id', 'name', 'is_active', 'job_center', 'is_deleted', 'created_at', 'updated_at', 'deleted_at']


admin.site.register(Country, CountryAdmin)
admin.site.register(ApplicationMethod, ApplicationMethodAdmin)
admin.site.register(BusinessActivity, BusinessActivityAdmin)
admin.site.register(CancellationReason, CancellationReasonAdmin)
admin.site.register(Cleaning, CleaningAdmin)
admin.site.register(Concept, ConceptAdmin)
admin.site.register(CustomDescription, CustomDescriptionAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Extra, ExtraAdmin)
admin.site.register(Indication, IndicationAdmin)
admin.site.register(InfestationDegree, InfestationDegreeAdmin)
admin.site.register(JobTitle, JobTitleAdmin)
admin.site.register(OriginSource, OriginSourceAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(PaymentWay, PaymentWayAdmin)
admin.site.register(PlagueCategory, PlagueCategoryAdmin)
admin.site.register(Plague, PlagueAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(PriceListPlague, PriceListPlagueAdmin)
admin.site.register(RejectionReason, RejectionReasonAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(TypeProduct, TypeProductAdmin)
admin.site.register(UnitProduct, UnitProductAdmin)
admin.site.register(Voucher, VoucherAdmin)
