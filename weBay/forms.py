from django import forms

class BidForm(forms.Form):
    bid_price = forms.FloatField()


class AuctionForm(forms.Form):
    owner = forms.CharField(max_length=200)
    name = forms.CharField(max_length=200)
    reserved_price = forms.FloatField()

    def process(self):
        cd = self.cleaned_data
        return cd

