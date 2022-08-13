from rest_framework.serializers import ModelSerializer

from apps.catalogs.models import *


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        exclude = ['is_deleted', 'deleted_at']


class ApplicationMethodSerializer(ModelSerializer):
    class Meta:
        model = ApplicationMethod
        exclude = ['is_deleted', 'deleted_at']


class BusinessActivitySerializer(ModelSerializer):
    class Meta:
        model = BusinessActivity
        exclude = ['is_deleted', 'deleted_at']


class CancellationReasonSerializer(ModelSerializer):
    class Meta:
        model = CancellationReason
        exclude = ['is_deleted', 'deleted_at']


class CleaningSerializer(ModelSerializer):
    class Meta:
        model = Cleaning
        exclude = ['is_deleted', 'deleted_at']


class ConceptSerializer(ModelSerializer):
    class Meta:
        model = Concept
        exclude = ['is_deleted', 'deleted_at']


class CustomDescriptionSerializer(ModelSerializer):
    class Meta:
        model = CustomDescription
        exclude = ['is_deleted', 'deleted_at']


class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        exclude = ['is_deleted', 'deleted_at']


class ExtraSerializer(ModelSerializer):
    class Meta:
        model = Extra
        exclude = ['is_deleted', 'deleted_at']


class IndicationSerializer(ModelSerializer):
    class Meta:
        model = Indication
        exclude = ['is_deleted', 'deleted_at']


class InfestationDegreeSerializer(ModelSerializer):
    class Meta:
        model = InfestationDegree
        exclude = ['is_deleted', 'deleted_at']


class JobTitleSerializer(ModelSerializer):
    class Meta:
        model = JobTitle
        exclude = ['is_deleted', 'deleted_at']


class OriginSourceSerializer(ModelSerializer):
    class Meta:
        model = OriginSource
        exclude = ['is_deleted', 'deleted_at']


class PaymentMethodSerializer(ModelSerializer):
    class Meta:
        model = PaymentMethod
        exclude = ['is_deleted', 'deleted_at']


class PaymentWaySerializer(ModelSerializer):
    class Meta:
        model = PaymentWay
        exclude = ['is_deleted', 'deleted_at']


class PlagueCategorySerializer(ModelSerializer):
    class Meta:
        model = PlagueCategory
        exclude = ['is_deleted', 'deleted_at']


class PlagueSerializer(ModelSerializer):
    class Meta:
        model = Plague
        exclude = ['is_deleted', 'deleted_at']


class PresentationSerializer(ModelSerializer):
    class Meta:
        model = Presentation
        exclude = ['is_deleted', 'deleted_at']


class ServiceTypeSerializer(ModelSerializer):
    class Meta:
        model = ServiceType
        exclude = ['is_deleted', 'deleted_at']


class PriceListSerializer(ModelSerializer):
    class Meta:
        model = PriceList
        exclude = ['is_deleted', 'deleted_at']


class PriceListPlagueSerializer(ModelSerializer):
    class Meta:
        model = PriceListPlague
        exclude = ['is_deleted', 'deleted_at']


class RejectionReasonSerializer(ModelSerializer):
    class Meta:
        model = RejectionReason
        exclude = ['is_deleted', 'deleted_at']


class StatusSerializer(ModelSerializer):
    class Meta:
        model = Status
        exclude = ['is_deleted', 'deleted_at']


class TaxSerializer(ModelSerializer):
    class Meta:
        model = Tax
        exclude = ['is_deleted', 'deleted_at']


class TypeProductSerializer(ModelSerializer):
    class Meta:
        model = TypeProduct
        exclude = ['is_deleted', 'deleted_at']


class UnitProductSerializer(ModelSerializer):
    class Meta:
        model = UnitProduct
        exclude = ['is_deleted', 'deleted_at']


class VoucherSerializer(ModelSerializer):
    class Meta:
        model = Voucher
        exclude = ['is_deleted', 'deleted_at']
