from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inventory.views import custom_404_view, CustomLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Admin Panel
    path('', include(('inventory.urls', 'inventory'), namespace="inventory")),  # ✅ Use proper namespace
    
    # ✅ Fix Logout Issue
    path("accounts/logout/", CustomLogoutView.as_view(), name="logout"),
]

# ✅ Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# ✅ Custom 404 page
handler404 = 'inventory.views.custom_404_view'
