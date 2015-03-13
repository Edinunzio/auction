from django import forms

class BidForm(forms.Form):
    bid_price = forms.DecimalField(max_digits=10, decimal_places=2)

