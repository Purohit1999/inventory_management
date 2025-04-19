from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "inventory"

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_product, name='add_product'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('upload/', views.upload_file, name='upload_file'),
    path('download/', views.download_file, name='download_file'),
    path('products/', views.product_list, name='product_list'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact'),

    # Auth views
    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)