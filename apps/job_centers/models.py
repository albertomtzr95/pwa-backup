from django.db import models

from apps.base.models import BaseModel


class JobCenter(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    health_manager = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(to='companies.Company', on_delete=models.CASCADE)
    taxpayer_registration = models.CharField(max_length=255, blank=True, null=True)
    license_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.CharField(max_length=50, blank=True, null=True)
    web_page = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    messenger = models.CharField(max_length=255, blank=True, null=True)
    sanitary_license = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
