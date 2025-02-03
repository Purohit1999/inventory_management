from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)  # ✅ Allow blank descriptions
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # ✅ Added default price

    def __str__(self):
        return self.name

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_received = models.IntegerField(default=0)
    date_received = models.DateTimeField(auto_now_add=True)
    stock_left = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.stock_left} left"

class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    total_order = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.total_order}"

class Transaction(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sold_to = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_sold = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sold_to} bought {self.product.name} for {self.amount}"
