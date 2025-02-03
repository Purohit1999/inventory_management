from django.contrib import admin
from django.urls import path, include
from inventory.views import home, upload_excel, inventory_management  # ✅ Import inventory_management


urlpatterns = [
    path('', home, name='home'),  # ✅ Home route
    path('admin/', admin.site.urls),  # ✅ Django admin
    path('upload-excel/', upload_excel, name='upload_excel'),  # ✅ Excel upload
    path('api/', include('inventory.urls')),  # ✅ Include API routes
    path('inventory/', inventory_management, name='inventory_management'),  # ✅ Fix inventory route
]
