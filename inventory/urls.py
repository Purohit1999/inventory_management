from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Ensure views is properly imported

# Create a router for API endpoints
router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'stock', views.StockViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'transactions', views.TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-excel/', views.upload_excel, name='upload_excel'),
    path('inventory/', views.inventory_management, name='inventory_management'),
]
