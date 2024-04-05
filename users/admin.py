from django.contrib import admin
from django.contrib.auth.models import Permission

from users.models import User


class CustomPermissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'content_type']


admin.site.register(Permission, CustomPermissionAdmin)
admin.site.register(User)
