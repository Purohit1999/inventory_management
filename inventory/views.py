from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib.auth.views import LogoutView
from django.utils.decorators import method_decorator

import pandas as pd

from .models import Product
from .forms import ProductForm, UploadFileForm


# ===========================
# ✅ Home Page View
# ===========================

def home(request):
    """ Displays all products. """
    products = Product.objects.all()
    return render(request, 'inventory/home.html', {'products': products})


# ===========================
# ✅ Product CRUD Operations
# ===========================

@login_required
def add_product(request):
    """ Add a new product manually through a form. """
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Product added successfully!")
            return redirect('inventory:product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})


@login_required
def update_product(request, product_id):
    """ Update an existing product. """
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Product updated successfully!")
            return redirect('inventory:product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'inventory/update_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request, product_id):
    """ Delete a product """
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "❌ Product deleted successfully!")
    return redirect('inventory:product_list')


# ===========================
# ✅ File Upload & Download
# ===========================

@login_required
def upload_file(request):
    """ Handles Excel/CSV file upload and adds products to the database. """
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]

        # Validate file type
        allowed_extensions = ('.csv', '.xls', '.xlsx')
        if not uploaded_file.name.endswith(allowed_extensions):
            messages.error(request, "⚠ Invalid file format! Please upload a CSV or Excel file.")
            return redirect("inventory:upload_file")

        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            # Validate required columns
            required_columns = {"name", "description", "price", "stock", "category"}
            if not required_columns.issubset(df.columns):
                messages.error(request, "⚠ Invalid file structure. Please check column headers.")
                return redirect("inventory:upload_file")

            # Insert products into database (check for duplicates)
            for _, row in df.iterrows():
                Product.objects.update_or_create(
                    name=row["name"],
                    defaults={
                        "description": row.get("description", ""),
                        "price": row["price"],
                        "stock": row["stock"],
                        "category": row["category"],
                    },
                )

            messages.success(request, "✅ File uploaded successfully!")
        except Exception as e:
            messages.error(request, f"❌ Error uploading file: {e}")

        return redirect("inventory:upload_file")

    return render(request, "inventory/upload_file.html")


@login_required
def download_file(request):
    """ Generates a CSV file containing all products. """
    products = Product.objects.all().values("name", "description", "price", "stock", "category")

    if not products:
        messages.warning(request, "⚠ No products available to download.")
        return redirect("inventory:product_list")

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=inventory_products.csv'

    df = pd.DataFrame.from_records(products)
    df.to_csv(path_or_buf=response, index=False)

    return response


# ===========================
# ✅ Product List View
# ===========================

@login_required
def product_list(request):
    """ Displays the list of products with Edit/Delete options. """
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})


# ===========================
# ✅ Additional Pages
# ===========================

def about_page(request):
    """ Renders the About page. """
    return render(request, 'inventory/about.html')


# ===========================
# ✅ Authentication Views
# ===========================

def login_view(request):
    """ Handles user login. """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"✅ Welcome {username}!")
                return redirect('inventory:home')
            else:
                messages.error(request, "❌ Invalid username or password.")
        else:
            messages.error(request, "❌ Invalid form submission. Please check your input.")

    else:
        form = AuthenticationForm()

    return render(request, 'inventory/login.html', {'form': form})


# ✅ Custom Logout View (Fix Logout 405 Error)
@method_decorator(csrf_exempt, name='dispatch')
class CustomLogoutView(LogoutView):
    """ Allows both GET and POST requests for logout """
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


# ===========================
# ✅ Custom Error Pages
# ===========================

def custom_404_view(request, exception):
    """ Custom 404 error page """
    return render(request, "inventory/404.html", status=404)
