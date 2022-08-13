from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from django.utils.text import slugify

from apps.base.pagination import StandardResultsSetPagination
from apps.companies.serializers import *
from apps.base import folios


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanyCreateSerializer
    queryset = CompanySerializer.Meta.model.objects.order_by('-created_at').filter(is_deleted=False)
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        request.data['folio'] = folios.company()
        request.data['slug'] = slugify(request.data['name'])
        serializer = CompanyCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        company = self.get_queryset().filter(id=self.kwargs['pk']).first()
        if company:
            company.is_deleted = True
            company.save()
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        return Response(data={'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
