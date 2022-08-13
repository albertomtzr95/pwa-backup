"""
core URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from apps.users.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authentication/login/', Login.as_view(), name='token_obtain_pair'),
    path('api/authentication/logout/', Logout.as_view(), name='logout'),
    path('api/authentication/refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('apps.users.routers')),
    path('api/catalogs/', include('apps.catalogs.routers')),
    path('api/', include('apps.companies.routers')),
]
