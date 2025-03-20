from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from inventory.views import custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Admin Panel

    # ✅ Includes Inventory App URLs
    path('', include(('inventory.urls', 'inventory'), namespace="inventory")),

    # ✅ Fix: Explicitly allow GET method for logout
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/logout/get/', LogoutView.as_view(), name='logout_get'),
]

# ✅ Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# ✅ Custom 404 Error Handler
handler404 = 'inventory.views.custom_404_view'
