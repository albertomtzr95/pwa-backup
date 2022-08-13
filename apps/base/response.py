from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


def validation_error(detail, code=status.HTTP_400_BAD_REQUEST):
    raise ValidationError({'detail': detail}, code=code)


def response(data=None, code=status.HTTP_200_OK, message=''):
    return Response({
        'data': data,
        'code': code,
        'message': message
    }, status=code)
