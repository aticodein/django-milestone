from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=254, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
