from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.catalogs.serializers import *
from apps.base.pagination import StandardResultsSetPagination


class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = CountrySerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class ApplicationMethodViewSet(ModelViewSet):
    serializer_class = ApplicationMethodSerializer
    queryset = ApplicationMethodSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class BusinessActivityViewSet(ModelViewSet):
    serializer_class = BusinessActivitySerializer
    queryset = BusinessActivitySerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class CancellationReasonViewSet(ModelViewSet):
    serializer_class = CancellationReasonSerializer
    queryset = CancellationReasonSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class CleaningViewSet(ModelViewSet):
    serializer_class = CleaningSerializer
    queryset = CleaningSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class ConceptViewSet(ModelViewSet):
    serializer_class = ConceptSerializer
    queryset = ConceptSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class CustomDescriptionViewSet(ModelViewSet):
    serializer_class = CustomDescriptionSerializer
    queryset = CustomDescriptionSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class DiscountViewSet(ModelViewSet):
    serializer_class = DiscountSerializer
    queryset = DiscountSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class ExtraViewSet(ModelViewSet):
    serializer_class = ExtraSerializer
    queryset = ExtraSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class IndicationViewSet(ModelViewSet):
    serializer_class = IndicationSerializer
    queryset = IndicationSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class InfestationDegreeViewSet(ModelViewSet):
    serializer_class = InfestationDegreeSerializer
    queryset = InfestationDegreeSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class JobTitleViewSet(ModelViewSet):
    serializer_class = JobTitleSerializer
    queryset = JobTitleSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class OriginSourceViewSet(ModelViewSet):
    serializer_class = OriginSourceSerializer
    queryset = OriginSourceSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class PaymentMethodViewSet(ModelViewSet):
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethodSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class PaymentWayViewSet(ModelViewSet):
    serializer_class = PaymentWaySerializer
    queryset = PaymentWaySerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class PlagueCategoryViewSet(ModelViewSet):
    serializer_class = PlagueCategorySerializer
    queryset = PlagueCategorySerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class PlagueViewSet(ModelViewSet):
    serializer_class = PlagueSerializer
    queryset = PlagueSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class PresentationViewSet(ModelViewSet):
    serializer_class = PresentationSerializer
    queryset = PresentationSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class ServiceTypeViewSet(ModelViewSet):
    serializer_class = ServiceTypeSerializer
    queryset = ServiceTypeSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class PriceListViewSet(ModelViewSet):
    serializer_class = PriceListSerializer
    queryset = PriceListSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class PriceListPlagueViewSet(ModelViewSet):
    serializer_class = PriceListPlagueSerializer
    queryset = PriceListPlagueSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class RejectionReasonViewSet(ModelViewSet):
    serializer_class = RejectionReasonSerializer
    queryset = RejectionReasonSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class StatusViewSet(ModelViewSet):
    serializer_class = StatusSerializer
    queryset = StatusSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class TaxViewSet(ModelViewSet):
    serializer_class = TaxSerializer
    queryset = TaxSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class TypeProductViewSet(ModelViewSet):
    serializer_class = TypeProductSerializer
    queryset = TypeProductSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class UnitProductViewSet(ModelViewSet):
    serializer_class = UnitProductSerializer
    queryset = UnitProductSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


class VoucherViewSet(ModelViewSet):
    serializer_class = VoucherSerializer
    queryset = VoucherSerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def destroy(self, request, *args, **kwargs):
        catalog = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if catalog:
            catalog.is_deleted = True
            catalog.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
