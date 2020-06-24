from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('image',)}),)
    list_display = ['email', 'username', 'image']


admin.site.register(CustomUser, CustomUserAdmin)
