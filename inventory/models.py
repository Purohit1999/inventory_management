from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('home', 'Home & Kitchen'),
        ('sports', 'Sports'),
        ('books', 'Books'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)  # Added default to avoid NULL errors
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Products"  # Proper admin panel name

    def __str__(self):
        return f"{self.name} - {self.category}"
