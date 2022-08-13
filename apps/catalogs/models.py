from django.db import models

from apps.base.models import BaseModel, CatalogModel


class Country(BaseModel):
    name = models.CharField(max_length=255)
    code_country = models.CharField(max_length=255)
    coin_country = models.CharField(max_length=255)
    symbol_country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ApplicationMethod(CatalogModel):
    pass


class BusinessActivity(CatalogModel):
    pass


class CancellationReason(CatalogModel):
    pass


class Cleaning(CatalogModel):
    pass


class Concept(BaseModel):
    EXPENSE = 'EX'
    ORDER = 'OR'
    TYPES_CHOICES = [
        (EXPENSE, 'Gasto'),
        (ORDER, 'Orden de Compra'),
    ]
    name = models.CharField(max_length=255)
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPES_CHOICES, default=EXPENSE)

    def __str__(self):
        return self.name


class CustomDescription(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Discount(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    percentage = models.SmallIntegerField()
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Extra(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Indication(BaseModel):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    description = models.TextField()
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class InfestationDegree(CatalogModel):
    pass


class JobTitle(CatalogModel):
    pass


class OriginSource(CatalogModel):
    pass


class PaymentMethod(CatalogModel):
    pass


class PaymentWay(BaseModel):
    name = models.CharField(max_length=255)
    credit_days = models.PositiveSmallIntegerField(default=0)
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PlagueCategory(CatalogModel):
    pass


class Plague(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(to='catalogs.PlagueCategory', on_delete=models.CASCADE)
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Presentation(CatalogModel):
    pass


class ServiceType(BaseModel):
    name = models.CharField(max_length=255)
    frequency_days = models.PositiveSmallIntegerField(default=0)
    certificate_expiration_days = models.PositiveSmallIntegerField(default=0)
    follow_up_days = models.PositiveSmallIntegerField(default=0)
    disinfection = models.BooleanField(default=False)
    show_price = models.BooleanField(default=True)
    cover = models.CharField(max_length=255, blank=True, null=True)
    indication_id = models.ForeignKey(to='catalogs.Indication', on_delete=models.CASCADE)
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PriceList(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(to='catalogs.PlagueCategory', on_delete=models.CASCADE)
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    hierarchy = models.PositiveSmallIntegerField()
    cost = models.FloatField()
    min_cost = models.FloatField()
    service_type_id = models.ForeignKey(to='catalogs.ServiceType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PriceListPlague(BaseModel):
    price_list = models.ForeignKey(to='catalogs.PriceList', on_delete=models.CASCADE)
    plague = models.ForeignKey(to='catalogs.Plague', on_delete=models.CASCADE)
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)


class RejectionReason(CatalogModel):
    pass


class Status(BaseModel):
    COMPANY = 'CO'
    CUSTOMERS = 'CU'
    EMPLOYEES = 'EM'
    QUOTES = 'QO'
    EVENTS = 'EV'
    STATUS_CHOICES = [
        (COMPANY, 'Companies'),
        (CUSTOMERS, 'Customers'),
        (EMPLOYEES, 'Employees'),
        (QUOTES, 'Quotes'),
        (EVENTS, 'Events'),
    ]
    name = models.CharField(max_length=255)
    key_string = models.CharField(max_length=100)
    module = models.CharField(max_length=2, choices=STATUS_CHOICES, default=COMPANY)

    def __str__(self):
        return self.name


class Tax(BaseModel):
    name = models.CharField(max_length=255)
    value = models.SmallIntegerField(default=16)
    is_main = models.BooleanField(default=False)
    job_center = models.ForeignKey(to='job_centers.JobCenter', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TypeProduct(CatalogModel):
    pass


class UnitProduct(CatalogModel):
    pass


class Voucher(CatalogModel):
    pass
