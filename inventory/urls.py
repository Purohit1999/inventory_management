from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    home, add_product, update_product, delete_product,
    upload_file, download_file, product_list, about_page  # ✅ Removed contact_page
)

# ✅ Namespace for the app
app_name = "inventory"

urlpatterns = [
    path('', home, name='home'),  # ✅ Home route
    path('add/', add_product, name='add_product'),
    path('update/<int:product_id>/', update_product, name='update_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('upload/', upload_file, name='upload_file'),
    path('download/', download_file, name='download_file'),  # ✅ Download route
    path('products/', product_list, name='product_list'),
    path('about/', about_page, name='about_page'),
     path('contact/', views.contact_page, name='contact'),

    # ✅ Authentication Views
    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# ✅ Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
