from django.db import models
from category.models import Category
from datetime import datetime, date

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=254, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='images')
    startingBidPrice = models.DecimalField(max_digits=9, decimal_places=2)
    # highestBidPrice = models.DecimalField(max_digits=9, decimal_places=2)
    # currentBidPrice =  models.DecimalField(max_digits=9, decimal_places=2)
    auctionEndDate = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)

    def __str__(self):
        return self.description
