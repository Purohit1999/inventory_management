from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from inventory.views import custom_404_view  # ✅ Custom 404 Page

urlpatterns = [
    # ✅ Django Admin
    path('admin/', admin.site.urls),

    # ✅ Includes Inventory App URLs (Namespace added)
    path('', include(('inventory.urls', 'inventory'), namespace="inventory")),

    # ✅ Logout using Django's built-in view (Fixes 405 Error)
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]

# ✅ Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# ✅ Custom Error Handlers
handler404 = 'inventory.views.custom_404_view'
