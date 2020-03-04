from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Auction(models.Model):

    name = models.CharField(max_length=254, default='')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    user_bid = ('users_last_bid')
    current_highest_bid = ('highest bid from all users in auction')
    base_bid = models.DecimalField(max_digits=9, decimal_places=2, default='50.00')
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    product_image = models.ImageField(upload_to='auction.images', default='')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)
    description = models.TextField()
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()
    number_of_bids = models.IntegerField()
    
    
    def __str__(self):
        return self.name
