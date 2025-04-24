from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts import models


class CustomUserAdmin(UserAdmin):
    """Custom User Admin for the BaseUser model."""

    list_display = ("email", "username", "is_staff", "is_active")
    list_filter = ("email", "username", "is_staff", "is_active")
    search_fields = ("email", "username")
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(models.BaseUser, CustomUserAdmin)
