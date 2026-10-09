
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey( Category, on_delete=models.CASCADE, related_name="products" )
    def __str__(self):
        return self.title