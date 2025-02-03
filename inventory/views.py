from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render
import pandas as pd
from .models import Product, Stock, Order, Transaction
from .serializers import ProductSerializer, StockSerializer, OrderSerializer, TransactionSerializer

def home(request):
    return HttpResponse("<h1>Welcome to the Inventory Management System</h1>")

def inventory_management(request):
    return render(request, 'inventory/inventory_management.html')  # ✅ Ensure this file exists

def upload_excel(request):
    if request.method == "POST" and request.FILES.get("excel_file"):
        excel_file = request.FILES["excel_file"]

        try:
            df = pd.read_excel(excel_file, engine="openpyxl")
        except Exception as e:
            return HttpResponse(f"Error reading Excel file: {str(e)}", status=400)

        if df.empty:
            return HttpResponse("Uploaded file is empty!", status=400)

        for _, row in df.iterrows():
            product_name = row.get("Product Name", "").strip()

            if product_name:
                product, _ = Product.objects.get_or_create(
                    name=product_name,
                    defaults={"description": row.get("Description", ""), "price": row.get("Price (£)", 0)}
                )

                if "Quantity Received" in df.columns and not pd.isna(row.get("Quantity Received")):
                    Stock.objects.create(
                        product=product,
                        quantity_received=row.get("Quantity Received", 0),
                        stock_left=row.get("Stock Left", 0)
                    )

                if "Customer Name" in df.columns and row.get("Customer Name"):
                    order = Order.objects.create(  # ✅ Assign order instance
                        customer_name=row["Customer Name"],
                        total_order=row.get("Total Order (£)", 0)
                    )

                    if "Sold To" in df.columns and row.get("Sold To"):
                        Transaction.objects.create(  # ✅ Link to `order`
                            order=order,
                            product=product,
                            sold_to=row["Sold To"],
                            amount=row.get("Amount (£)", 0)
                        )

        return HttpResponse("Excel file uploaded successfully!")

    return TemplateResponse(request, "inventory/upload_excel.html")

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
