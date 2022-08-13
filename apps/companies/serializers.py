from rest_framework import serializers

from apps.catalogs.serializers import CountrySerializer
from apps.companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Company
        exclude = ['is_deleted', 'deleted_at']


class CompanyCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['folio', 'name', 'slug', 'contact_name', 'contact_email', 'contact_phone', 'country', 'web_color']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'folio': instance.folio,
            'name': instance.name,
            'slug': instance.slug,
            'contact_name': instance.contact_name,
            'contact_email': instance.contact_email,
            'contact_phone': instance.contact_phone,
            'country': {
                'id': instance.country.id,
                'name': instance.country.name,
                'code_country': instance.country.code_country,
                'coin_country': instance.country.coin_country,
                'symbol_country': instance.country.symbol_country,
                'created_at': instance.country.created_at,
                'updated_at': instance.country.updated_at,
            },
            'document_logo': instance.document_logo,
            'document_stamp': instance.document_stamp,
            'web_logo': instance.web_logo,
            'web_color': instance.web_color,
            'cutoff_date': instance.cutoff_date,
            'is_active': instance.is_active,
            'created_at': instance.created_at,
            'updated_at': instance.updated_at
        }
