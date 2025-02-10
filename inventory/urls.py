from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    home, add_product, update_product, delete_product,
    upload_file, product_list, about_page, login_view, logout_view
)

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_product, name='add_product'),
    path('update/<int:product_id>/', update_product, name='update_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('upload/', upload_file, name='upload_file'),
    path('products/', product_list, name='product_list'),
    path('about/', about_page, name='about_page'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
