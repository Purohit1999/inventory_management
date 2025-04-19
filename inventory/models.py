from django.db import models
from django.urls import reverse


class Product(models.Model):
    """
    Represents a product in the inventory system.
    """

    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('home', 'Home & Kitchen'),
        ('sports', 'Sports & Fitness'),
        ('books', 'Books & Stationery'),
        ('other', 'Other'),
    ]

    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Unique product name."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional product description."
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Product price in currency."
    )
    stock = models.PositiveIntegerField(
        default=0,
        help_text="Units available in inventory."
    )
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='other',
        help_text="Select the category that best fits the product."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the product was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the product was last updated."
    )

    class Meta:
        verbose_name_plural = "Products"
        ordering = ['name']  # Alphabetical ordering by product name

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

    def get_absolute_url(self):
        return reverse("inventory:product_list")
