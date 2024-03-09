from django.contrib import admin

from catalog.models import Category, Products, Contacts


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', )


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'preview', 'category', 'price', 'created_at', 'updated_at', )
    list_filter = ('category', 'created_at', 'updated_at', )
    search_fields = ('name', 'last_name', 'category', )


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message',)
    search_fields = ('name', )
