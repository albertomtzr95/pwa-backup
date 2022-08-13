from django.db import models

from apps.base.models import BaseModel


class Company(BaseModel):
    folio = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    contact_phone = models.CharField(max_length=50)
    country = models.ForeignKey(to='catalogs.Country', on_delete=models.CASCADE)
    document_logo = models.CharField(max_length=255, blank=True, null=True)
    document_stamp = models.CharField(max_length=255, blank=True, null=True)
    web_logo = models.CharField(max_length=255, blank=True, null=True)
    web_color = models.CharField(max_length=50, default='#3C589')
    cutoff_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
