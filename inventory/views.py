from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse  # Import HttpResponse for homepage
from django.shortcuts import render
import pandas as pd
from .models import Product, Stock, Order, Transaction
from .serializers import ProductSerializer, StockSerializer, OrderSerializer, TransactionSerializer


def home(request):
    return HttpResponse("<h1>Welcome to the Inventory Management System</h1>")


def upload_excel(request):
    if request.method == "POST" and request.FILES.get("excel_file"):
        excel_file = request.FILES["excel_file"]
        df = pd.read_excel(excel_file, engine="openpyxl")

        for index, row in df.iterrows():
            if "Product Name" in df.columns:
                product, created = Product.objects.get_or_create(
                    name=row["Product Name"],
                    defaults={"description": row.get("Description", ""), "price": row.get("Price (£)", 0)},
                )

            if "Quantity Received" in df.columns:
                Stock.objects.create(
                    product=product,
                    quantity_received=row.get("Quantity Received", 0),
                    stock_left=row.get("Stock Left", 0)
                )

            if "Customer Name" in df.columns:
                Order.objects.create(
                    customer_name=row["Customer Name"],
                    total_order=row.get("Total Order (£)", 0)
                )

            if "Sold To" in df.columns:
                Transaction.objects.create(
                    customer_name=row["Customer Name"],
                    product=product,
                    sold_to=row.get("Sold To", ""),
                    amount=row.get("Amount (£)", 0)
                )

        return HttpResponse("Excel file uploaded and data inserted successfully!")

    return render(request, "upload_excel.html")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.