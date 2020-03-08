from django.shortcuts import reverse, redirect, get_object_or_404, render
from django.contrib import messages
from .models import Auction

# Create your views here.

def auction(request):
    auctions = Auction.objects.all()
    return render(request, "auction.html", {"auctions": auctions})

def raise_bid(request, id):
    """Adjust the bid for the specified product by the specified amount"""
    try:
        user_bid = int(request.POST.get('user_bid'))
    except:
        return redirect(reverse('auction'))
    
    if user_bid > 0:
        user_bid = user_bid
    else:
        messages.error(request, "Unable to take bid")

    return redirect(reverse('raise_bid'))    
