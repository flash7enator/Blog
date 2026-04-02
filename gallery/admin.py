from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at")
    ordering = ("title", "-uploaded_at")
    search_fields = ("title",)