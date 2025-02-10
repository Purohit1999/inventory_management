from django.contrib import admin
from .models import Product  # Import Product model

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'category')
    list_filter = ('category',)
