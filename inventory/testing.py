from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from inventory.models import Product
from inventory.forms import ProductForm, UploadFileForm
import tempfile
import pandas as pd


# ==========================
# ✅ Product Model Tests
# ==========================
class ProductModelTest(TestCase):
    """Tests for the Product model"""

    def setUp(self):
        """Set up a sample product for testing"""
        self.product = Product.objects.create(
            name="Test Product",
            description="This is a test product",
            price=50.99,
            stock=20,
            category="Electronics"
        )

    def test_product_creation(self):
        """Check if product is created correctly"""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.stock, 20)

    def test_product_str_method(self):
        """Ensure __str__ method returns the product name"""
        self.assertEqual(str(self.product), "Test Product")


# ==========================
# ✅ Product Form Tests
# ==========================
class ProductFormTest(TestCase):
    """Tests for Product form"""

    def test_valid_product_form(self):
        """Ensure a valid form submission works"""
        form_data = {
            'name': "Smartphone",
            'description': "A new smartphone",
            'price': 799.99,
            'stock': 10,
            'category': "Electronics"
        }
        form = ProductForm(data=form_data)
        self.assertTrue(form.is_valid())  # The form should be valid

    def test_invalid_product_form(self):
        """Ensure form fails validation when required fields are missing"""
        form_data = {
            'name': "",
            'description': "Invalid product",
            'price': "invalid_price",  # Price should be a number
            'stock': "invalid_stock"   # Stock should be a number
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())  # The form should not be valid


# ==========================
# ✅ File Upload Form Tests
# ==========================
class UploadFileFormTest(TestCase):
    """Tests for the UploadFile form"""

    def test_valid_file_upload_form(self):
        """Ensure form accepts valid CSV/Excel files"""
        temp_file = tempfile.NamedTemporaryFile(suffix=".csv")
        form = UploadFileForm(data={}, files={'file': temp_file})
        self.assertTrue(form.is_valid())  # The form should be valid

    def test_invalid_file_upload_form(self):
        """Ensure form fails if no file is uploaded"""
        form = UploadFileForm(data={}, files={})
        self.assertFalse(form.is_valid())  # The form should not be valid


# ==========================
# ✅ Product View Tests
# ==========================
class ProductViewTest(TestCase):
    """Tests for Product views"""

    def setUp(self):
        """Set up test user and sample product"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        self.product = Product.objects.create(
            name="Laptop",
            description="A high-end laptop",
            price=1200.99,
            stock=15,
            category="Electronics"
        )

    def test_home_page_view(self):
        """Ensure home page loads correctly"""
        response = self.client.get(reverse('inventory:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/home.html')

    def test_product_list_view(self):
        """Ensure product list page loads correctly"""
        response = self.client.get(reverse('inventory:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/product_list.html')

    def test_product_add_view(self):
        """Ensure product can be added successfully"""
        response = self.client.post(reverse('inventory:add_product'), {
            'name': "Tablet",
            'description': "A new tablet",
            'price': 399.99,
            'stock': 30,
            'category': "Electronics"
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Product.objects.count(), 2)  # Ensure product count increased

    def test_product_update_view(self):
        """Ensure product update works correctly"""
        response = self.client.post(reverse('inventory:update_product', args=[self.product.id]), {
            'name': "Updated Laptop",
            'description': "Updated description",
            'price': 1000.99,
            'stock': 10,
            'category': "Electronics"
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, "Updated Laptop")

    def test_product_delete_view(self):
        """Ensure product deletion works correctly"""
        response = self.client.post(reverse('inventory:delete_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Product.objects.count(), 0)  # Ensure product is deleted


# ==========================
# ✅ Authentication Tests
# ==========================
class AuthenticationTest(TestCase):
    """Tests for user authentication"""

    def setUp(self):
        """Set up a test user"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_login(self):
        """Ensure user can log in successfully"""
        response = self.client.post(reverse('inventory:login'), {
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        """Ensure user can log out successfully"""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('inventory:logout'))
        self.assertEqual(response.status_code, 302)  # Redirect after logout


# ==========================
# ✅ File Upload Tests
# ==========================
class FileUploadTest(TestCase):
    """Tests for CSV/Excel file upload"""

    def setUp(self):
        """Set up test user"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_upload_valid_csv(self):
        """Ensure CSV file upload works correctly"""
        csv_data = "name,description,price,stock,category\nPhone,New phone,500,10,Electronics"
        temp_file = tempfile.NamedTemporaryFile(mode='w+', suffix=".csv", delete=False)
        temp_file.write(csv_data)
        temp_file.seek(0)

        response = self.client.post(reverse('inventory:upload_file'), {'file': temp_file})
        temp_file.close()
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Product.objects.count(), 1)

    def test_upload_invalid_file_format(self):
        """Ensure invalid file formats are rejected"""
        temp_file = tempfile.NamedTemporaryFile(suffix=".txt")
        response = self.client.post(reverse('inventory:upload_file'), {'file': temp_file})
        self.assertEqual(response.status_code, 302)  # Should redirect due to error


# ==========================
# ✅ File Download Tests
# ==========================
class FileDownloadTest(TestCase):
    """Tests for CSV file download"""

    def setUp(self):
        """Set up test user and sample product"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

        Product.objects.create(name="Headphones", description="Wireless headphones", price=199.99, stock=50, category="Accessories")

    def test_download_csv(self):
        """Ensure inventory can be downloaded as CSV"""
        response = self.client.get(reverse('inventory:download_file'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv')
