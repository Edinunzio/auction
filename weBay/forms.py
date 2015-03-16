from django import forms
from django.shortcuts import get_list_or_404
from models import Item

class BidForm(forms.Form):
    bid_price = forms.DecimalField(max_digits=10, decimal_places=2)


class ItemForm(forms.Form):
    name = forms.CharField(max_length=200)
    reserved_price = forms.DecimalField(max_digits=10, decimal_places=2)


class AuctionForm(forms.Form):
    CHOICES = get_list_or_404(Item)
    status = forms.Select(choices=CHOICES)
