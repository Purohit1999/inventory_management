from django.contrib import admin
from .models import Product  # Import Product model

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Admin panel customization for managing products """
    
    # ✅ Fields displayed in the admin product list
    list_display = ('id', 'name', 'price', 'stock', 'category', 'created_at', 'updated_at')
    
    # ✅ Fields that support search functionality
    search_fields = ('name', 'category', 'description')
    
    # ✅ Filters available in the sidebar
    list_filter = ('category', 'created_at', 'updated_at')
    
    # ✅ Sorting by default (newest products first)
    ordering = ('-created_at',)
    
    # ✅ Fields that allow inline editing from the list view
    list_editable = ('price', 'stock', 'category')
    
    # ✅ Fields that are readonly (auto-generated fields)
    readonly_fields = ('created_at', 'updated_at')
    
    # ✅ Number of items per page in the admin list
    list_per_page = 20
    
    # ✅ Enable bulk delete & update actions
    actions = ['set_stock_to_zero']

    def set_stock_to_zero(self, request, queryset):
        """ Custom admin action to reset stock to zero for selected products """
        queryset.update(stock=0)
        self.message_user(request, "✅ Stock reset to zero for selected products.")
    
    set_stock_to_zero.short_description = "Set stock to zero for selected products"

