from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, StockViewSet, OrderViewSet, TransactionViewSet, upload_excel

# Create a router for API endpoints
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'stock', StockViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload-excel/', upload_excel, name='upload_excel'),
]