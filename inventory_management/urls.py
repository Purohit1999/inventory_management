from django.contrib import admin
from django.urls import path, include
from inventory.views import home  # Import the homepage view

urlpatterns = [
    path('', home, name='home'),  # Default homepage
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
]
