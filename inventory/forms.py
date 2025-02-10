from django import forms
from .models import Product
import pandas as pd

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category']

class UploadFileForm(forms.Form):
    file = forms.FileField()
