from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Product
from .forms import ProductForm, UploadFileForm
import pandas as pd


def home(request):
    """ Home view: Displays all products. """
    products = Product.objects.all()
    return render(request, 'inventory/home.html', {'products': products})


def add_product(request):
    """ Add a new product manually through a form. """
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Product added successfully!")
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})


def update_product(request, product_id):
    """ Update an existing product. """
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Product updated successfully!")
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'inventory/update_product.html', {'form': form, 'product': product})


def delete_product(request, product_id):
    """ Delete a product """
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "❌ Product deleted successfully!")
    return redirect('product_list')


def upload_file(request):
    """ Handles Excel/CSV file upload and adds products to the database. """
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]

        # Validate file type
        if not uploaded_file.name.endswith(('.csv', '.xls', '.xlsx')):
            messages.error(request, "⚠ Invalid file format! Please upload a CSV or Excel file.")
            return redirect("upload_file")

        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            # Validate required columns
            required_columns = {"name", "description", "price", "stock", "category"}
            if not required_columns.issubset(df.columns):
                messages.error(request, "⚠ Invalid file structure. Please check column headers.")
                return redirect("upload_file")

            # Insert into database
            for _, row in df.iterrows():
                Product.objects.create(
                    name=row["name"],
                    description=row.get("description", ""),
                    price=row["price"],
                    stock=row["stock"],
                    category=row["category"]
                )

            messages.success(request, "✅ File uploaded successfully!")
        except Exception as e:
            messages.error(request, f"❌ Error uploading file: {e}")

        return redirect("upload_file")

    return render(request, "inventory/upload.html")


def product_list(request):
    """ Displays the list of products with Edit/Delete options. """
    products = Product.objects.all()
    return render(request, 'inventory/products.html', {'products': products})


def about_page(request):
    """ Renders the About page. """
    return render(request, 'inventory/about.html')


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
                return redirect('home')  # Redirect to home after login
            else:
                messages.error(request, "❌ Invalid username or password.")
        else:
            messages.error(request, "❌ Invalid form submission. Please check your input.")

    else:
        form = AuthenticationForm()

    return render(request, 'inventory/login.html', {'form': form})


def logout_view(request):
    """ Handles user logout. """
    logout(request)
    messages.success(request, "✅ Successfully logged out.")
    return redirect('login')
