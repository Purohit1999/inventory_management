import pandas as pd
from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse
from .models import Product, Stock, Order, Transaction

class ProductAdmin(admin.ModelAdmin):
    change_list_template = "admin/upload_excel.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-excel/', self.admin_site.admin_view(self.upload_excel), name="upload_excel"),
        ]
        return custom_urls + urls

    def upload_excel(self, request):
        if request.method == "POST" and request.FILES.get("excel_file"):
            excel_file = request.FILES["excel_file"]
            df = pd.read_excel(excel_file, engine="openpyxl")

            for _, row in df.iterrows():
                product, _ = Product.objects.get_or_create(
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

            return HttpResponse("Excel file uploaded successfully!")

        return render(request, "admin/excel_upload.html")

admin.site.register(Product, ProductAdmin)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(Transaction)
