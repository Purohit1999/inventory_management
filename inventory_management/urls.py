from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inventory.views import custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Admin Panel
    path('', include('inventory.urls', namespace="inventory")),  # ✅ Includes Inventory App URLs
    path('', include(('inventory.urls', 'inventory'), namespace="inventory")),  # ✅ Added namespace
]

# ✅ Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# ✅ Optional: Redirect unknown URLs to home (helps prevent 404 errors)
handler404 = 'inventory.views.custom_404_view'
