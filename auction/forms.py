from django import forms
from .models import Bid


class AuctionUserBidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['user_bid']