from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Stock, Order, Transaction

class InventoryTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", description="Test Description", price=100.00)
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.order = Order.objects.create(customer_name="John Doe", total_order=500.00)
        self.stock = Stock.objects.create(product=self.product, quantity_received=50, stock_left=50)
        self.transaction = Transaction.objects.create(order=self.order, product=self.product, sold_to="Jane Doe", amount=100.00)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")

    def test_order_total(self):
        self.assertEqual(self.order.total_order, 500.00)

    def test_stock_quantity(self):
        self.assertEqual(self.stock.stock_left, 50)

    def test_transaction_amount(self):
        self.assertEqual(self.transaction.amount, 100.00)
from django.test import TestCase

# Create your tests here.
