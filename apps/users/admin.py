from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.users.models import User


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['name', 'username', 'role', 'is_active', 'is_verified', 'is_staff', 'is_superuser', 'is_deleted', 'last_login',
                    'created_at', 'updated_at']
    fieldsets = (
        (None, {'fields': ('name', 'first_name', 'username', 'password', 'role',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_verified',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'is_deleted',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login', 'created_at', 'updated_at',)}),
    )
    readonly_fields = ['last_login', 'created_at', 'updated_at']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'first_name',
                'username',
                'password1',
                'password2',
                'role',
                'is_verified',
                'is_active',
                'is_staff',
                'is_superuser',
                'is_deleted',
            )
        }),
    )


admin.site.register(User, UserAdmin)
