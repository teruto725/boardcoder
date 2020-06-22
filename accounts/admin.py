from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):#管理者画面用クラス（useradminを継承してる？ふつうはmodeladmin)
    model = CustomUser#ここも謎たぶんuseradminの仕様


admin.site.register(CustomUser, CustomUserAdmin)