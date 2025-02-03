from django.contrib import admin
from django.urls import path, include
from inventory.views import home, upload_excel

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('upload-excel/', upload_excel, name='upload_excel'),
    path('api/', include('inventory.urls')),
]
