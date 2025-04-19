from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.contrib.auth.views import LogoutView
from django.utils.decorators import method_decorator
import pandas as pd
from .models import Product
from .forms import ProductForm, UploadFileForm

def home(request):
    products = Product.objects.all()
    return render(request, "inventory/home.html", {"products": products})

def contact_page(request):
    return render(request, "inventory/contact.html")

def about_page(request):
    return render(request, "inventory/about.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, "inventory/product_list.html", {"products": products})

def download_file(request):
    products = Product.objects.all().values("name", "description", "price", "stock", "category")
    if not products:
        messages.warning(request, "⚠ No products available to download.")
        return redirect("inventory:product_list")

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=inventory_products.csv"
    df = pd.DataFrame.from_records(products)
    df.to_csv(path_or_buf=response, index=False)
    return response

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"✅ Welcome {user.username}!")
                return redirect("inventory:product_list")  # Redirect to product list after login
            else:
                messages.error(request, "❌ Invalid credentials.")
        else:
            messages.error(request, "❌ Please correct the errors below.")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})  # Use correct template path

@method_decorator(csrf_exempt, name="dispatch")
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Product added successfully!")
            return redirect("inventory:product_list")
    else:
        form = ProductForm()
    return render(request, "inventory/add_product.html", {"form": form})

@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Product updated successfully!")
            return redirect("inventory:product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "inventory/update_product.html", {"form": form, "product": product})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    messages.success(request, "❌ Product deleted successfully!")
    return redirect("inventory:product_list")

@login_required
def upload_file(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        allowed_extensions = (".csv", ".xls", ".xlsx")
        if not uploaded_file.name.endswith(allowed_extensions):
            messages.error(request, "⚠ Invalid file format! Please upload CSV or Excel.")
            return redirect("inventory:upload_file")
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            required_columns = {"name", "description", "price", "stock", "category"}
            if not required_columns.issubset(df.columns):
                messages.error(request, "⚠ Missing required columns. Please check file headers.")
                return redirect("inventory:upload_file")

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
            messages.success(request, "✅ File uploaded and processed!")
        except Exception as e:
            messages.error(request, f"❌ Upload error: {e}")
        return redirect("inventory:upload_file")
    return render(request, "inventory/upload_file.html")

def custom_404_view(request, exception):
    return render(request, "inventory/404.html", status=404)
