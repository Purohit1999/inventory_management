from django import forms
from .models import Product

# ==============================
# ✅ Product Form (For Adding/Updating Products)
# ==============================

class ProductForm(forms.ModelForm):
    """ Form for Adding/Updating a Product """

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter product description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter stock quantity'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category'}),
        }


# ==============================
# ✅ File Upload Form (For CSV/Excel)
# ==============================

class UploadFileForm(forms.Form):
    """ Form for Uploading CSV/Excel Files """
    
    file = forms.FileField(
        label="Upload CSV/Excel File",
        help_text="Only .csv, .xls, or .xlsx files are allowed.",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
    )

    def clean_file(self):
        """ Validate file type to allow only CSV and Excel files """
        file = self.cleaned_data.get('file')

        allowed_extensions = ['.csv', '.xls', '.xlsx']
        if file:
            file_name = file.name.lower()
            if not any(file_name.endswith(ext) for ext in allowed_extensions):
                raise forms.ValidationError("⚠ Invalid file format! Please upload a CSV or Excel file.")

        return file
