from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('header', 'preview', 'created_at', 'is_active',)
    search_fields = ('header', 'created_at',)
    list_filter = ('is_active',)
