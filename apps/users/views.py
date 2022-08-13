from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.base.response import response
from apps.users.models import User
from apps.users.serializers import CustomTokenObtainPairSerializer, UserSerializer


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = None

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class().Meta.model.objects.filter(is_active=True)
        return self.queryset

    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(username=username, password=password)

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserSerializer(user)
                data = {
                    'access_token': login_serializer.validated_data.get('access'),
                    'refresh_token': login_serializer.validated_data.get('refresh'),
                    'type': 'Bearer',
                    'user': user_serializer.data
                }
                return response(data=data, message='Bienvenido, sus credenciales son correctas.')
            return response(message='Las credenciales son incorrectas.', code=status.HTTP_400_BAD_REQUEST)
        return response(message='Las credenciales son incorrectas.', code=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    @classmethod
    def post(cls, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user', 0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return response(message='Sesión cerrada correctamente.')
        return response(message='No existe este usuario', code=status.HTTP_400_BAD_REQUEST)
