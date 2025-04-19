from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

# ✅ Import custom views
from inventory import views
from inventory.views import contact_page, custom_404_view

urlpatterns = [
    # ✅ Django Admin Panel
    path('admin/', admin.site.urls),

    # ✅ Inventory App URLs (including home page at '/')
    path('', include(('inventory.urls', 'inventory'), namespace='inventory')),

    # ✅ Contact Page Route
    path('contact/', contact_page, name='contact'),

    # ✅ Auth Routes
    path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]

# ✅ Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ✅ Custom 404 error handler
handler404 = 'inventory.views.custom_404_view'
