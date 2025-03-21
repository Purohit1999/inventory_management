from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

# ✅ Custom 404 view from your inventory app
from inventory.views import custom_404_view

urlpatterns = [
    # ✅ Django Admin Panel
    path('admin/', admin.site.urls),

    # ✅ Main App Routes (with namespace for reverse URL lookups)
    path('', include(('inventory.urls', 'inventory'), namespace='inventory')),

    # ✅ Secure logout (requires POST, used in base.html)
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]

# ✅ Serve static and media files during development only
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ✅ Custom error handler (optional but useful for Heroku/production)
handler404 = 'inventory.views.custom_404_view'
