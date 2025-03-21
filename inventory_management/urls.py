from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

# ✅ Import views correctly
from inventory import views  # Import views module properly
from inventory.views import contact_page, custom_404_view  # Corrected import

urlpatterns = [
    # ✅ Django Admin Panel
    path('admin/', admin.site.urls),

    # ✅ Main App Routes (with namespace for reverse URL lookups)
    path('', include(('inventory.urls', 'inventory'), namespace='inventory')),

    # ✅ Contact Page Route
    path('contact/', contact_page, name='contact'),

    # ✅ Secure logout (requires POST, used in base.html)
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]

# ✅ Serve static and media files during development only
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ✅ Custom error handler (optional but useful for Heroku/production)
handler404 = 'inventory.views.custom_404_view'
