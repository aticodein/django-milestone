from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.

class Auction(models.Model):

    name = models.CharField(max_length=254, default='')
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    current_highest_bid = ('highest bid from all users in auction')
    Product.startingBidPrice = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    product_image = models.ImageField(upload_to='auction.images', default='')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)
    description = models.TextField()
    time_starting = models.DateTimeField()
    time_ending = models.DateTimeField()
    number_of_bids = models.IntegerField()

    def __str__(self):
        return self.name

class Bid(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='auctions')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)
    user_bid = models.IntegerField(default='')

    def __int__(self):
        return self.product_id

"""
class Profile(models.Model):
    auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='auctions') # 1: which auctions they have bid on,
    number_of_bids = models.IntegerField() # 2: how many times they have bid on that auction
    user_bid = models.IntegerField(default='') # 3: their bid price 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) # 4: user_id as ForeignKey
    

    def __int__(self):
        return self.auction_id
"""