from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from products.models import Product
from .models import Auction
from .models import Bid
from .forms import AuctionUserBidForm
# Create your views here.


def auction(request):
    auctions = Auction.objects.all()
    if request.method == "POST":
        form = AuctionUserBidForm(request.POST or None)
        if form.is_valid():
            auction = get_object_or_404(Auction, pk=request.POST['auction_id'])
            product = get_object_or_404(Product, pk=request.POST['product_id'])
            instance = form.save(commit=False)
            print(form.cleaned_data.get("user_bid")) # delete this line at production
            instance.user_id = request.user
            instance.auction_id = auction
            instance.product_id = product
            context = {
            'auctions': auctions,
            'form': form
            }
            instance.save()
        return render(request, "auction.html", context)
    else:
        form = AuctionUserBidForm()
        context = {
            'auctions': auctions,
            'form': form
        }
    return render(request, "auction.html", context)

def raise_bid(request, bid_id):
    bid_id = int(bid_id)
    try:
        bid_raise = Bid.objects.get(id = bid_id)
    except Bid.DoesNotExist:
        return redirect('auction')
    form = Auction.objects.all(request.POST or None, instance = bid_raise)
    if form.is_valid():
       form.save()
       return redirect('auction')
    return render(request, 'templates/auction.html', {'form': form})







"""
def auction(request):
    auctions = Auction.objects.all()
    form = AuctionUserBidForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("user_bid"))
        instance.user = request.user
        instance.save()

    context = {
        'form': form
    }
    return render(request, "auction.html", {'auctions': auctions}, context)
"""

# def auction(request):
#     auctions = Auction.objects.all()
#     return render(request, "auction.html", {'auctions': auctions})

"""
def raise_bid(request, id):
    Adjust the bid for the specified product by the specified amount
    try:
        user_bid = int(request.POST.get('user_bid'))
    except:
        return redirect(reverse('auction'))
    
    if user_bid > 0:
        user_bid = user_bid
    else:
        messages.error(request, "Unable to take bid")

    return redirect(reverse('raise_bid'))    
"""